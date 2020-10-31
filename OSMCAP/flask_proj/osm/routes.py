from flask import render_template, url_for, flash, redirect
from osm.forms import RegistrationForm,LoginForm, InfoForm
from osm.models import User, Info
from osm import app, db, bcrypt
from flask_login import login_user, current_user, logout_user
from sqlalchemy import func, desc

@app.route('/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('You have been logged in!')
            return redirect(url_for('form'))
        else:
            flash('Login Unsuccessful. Please check username and password')
    return render_template('index.html', form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You can log in!')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/form',methods=['GET','POST'])
def form():
    form = InfoForm()
    if form.validate_on_submit():
        percent = (int(form.paper_accessed.data))/(int(form.target.data))
        inf = Info(subject = form.subject.data, branch = form.branch.data, semester = form.semester.data, sem_type = form.sem_type.data, paper_type=form.paper_type.data, date_accessed = form.date_accessed.data, 
                    faculty=form.faculty.data,target = form.target.data,paper_accessed = form.paper_accessed.data,paper_moderated = form.paper_moderated.data,percent=(int(form.paper_accessed.data))*100/(int(form.target.data)) )
        db.session.add(inf)
        db.session.commit()
        return redirect(url_for('summary'))
    return render_template('form.html',form=form)


@app.route('/summary')
def summary():

    info = Info.query.with_entities(Info.branch,func.sum(Info.paper_accessed).label('paper'),
                                    func.sum(Info.paper_moderated).label('paper_m'),
                                    func.sum(Info.target).label('Total_Target'),
                                    ((func.sum(Info.paper_accessed)*100)/(func.sum(Info.target))).label('Total_percent')
                                    ).group_by(Info.branch).all()                                
    return render_template('table.html',info=info)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
