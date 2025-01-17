
from flask import render_template, request, redirect
from saleapp import dao, login
from saleapp import app,admin
from saleapp.decorators import annoymous_user
import cloudinary.uploader

from flask_login import login_user,logout_user,current_user,login_required


@app.route("/")
def index():
    cate_id = request.args.get('category_id')
    kw = request.args.get('keyword')
    products = dao.load_products(cate_id=cate_id, kw=kw)
    return render_template('index.html', products=products)


@app.route('/products/<int:product_id>')
def details(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)


@app.route('/login-admin', methods=['post'])
def admin_login():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
        return redirect('/admin')


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):

            #upload
            avatar =''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar =res['secure_url']
            # save user
            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=password,avatar=avatar)
                return redirect('/login')
            except:
                err_msg='He thong dang co loi, vui long quay lai sau'
        else:
            err_msg = "Mat Khau Khong Khop"
    return render_template('register.html', err_msg=err_msg)


@app.route('/login', methods=['get','post'])
@annoymous_user
def login_my_user():

    if request.method.__eq__('POST'):
        username=request.form['username']
        password=request.form['password']
        user = dao.auth_user(username=username,password=password)
        if user:
            login_user(user=user)
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')


@app.context_processor
def common_attr():
    categories = dao.load_categories()
    return {
        'categories': categories
    }


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
