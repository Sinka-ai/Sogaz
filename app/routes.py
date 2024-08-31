from app import app,db
from flask import render_template,redirect,url_for,flash,request
from app.forms import RegisterForm,LoginForm,MessageForm, ChatMessageForm
from app.models import User, Message
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists! Please use a different one.')
            return redirect(url_for('register'))

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data
        )

        db.session.add(new_user)
        db.session.commit()
        print('all right')
        flash('Congrats! Now you can login')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Now!', form=form)


@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        if user and password:
            login_user(user, remember=1)
            next_page = request.args.get('next')
            print('yess')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/messages')
@login_required
def messages():
    # Получаем все уникальные диалоги для текущего пользователя
    dialogues = db.session.query(User).join(Message,
                (Message.sender_id == User.id) | (Message.recipient_id == User.id)
               ).filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id)).distinct()
    return render_template('messages.html', dialogues=dialogues)


@app.route('/messages/<int:user_id>', methods=['GET', 'POST'])
@login_required
def chat(user_id):
    user = User.query.get_or_404(user_id)

    if user == current_user:
        flash("Вы не можете отправлять сообщения самому себе.")
        return redirect(url_for('messages'))

    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == user.id)) |
        ((Message.sender_id == user.id) & (Message.recipient_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()

    form = ChatMessageForm()
    if form.validate_on_submit():
        new_message = Message(sender_id=current_user.id, recipient_id=user.id, content=form.content.data)
        db.session.add(new_message)
        db.session.commit()
        flash('Ваше сообщение было отправлено!')
        return redirect(url_for('chat', user_id=user.id))

    return render_template('chat.html', user=user, messages=messages, form=form)

@app.route('/send_message', methods=['GET', 'POST'])
@login_required
def send_message():
    form = MessageForm()
    if form.validate_on_submit():
        recipient = User.query.filter_by(username=form.recipient.data).first()
        if recipient:
            message = Message(sender_id=current_user.id, recipient_id=recipient.id, content=form.content.data)
            db.session.add(message)
            db.session.commit()
            flash('Сообщение отправлено!')
            return redirect(url_for('messages'))
        else:
            flash('Пользователь не найден.')
    return render_template('send_message.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))