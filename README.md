# برنامه ToDo

این یک برنامه ساده ToDo است که با استفاده از Django 5.1 و Django REST Framework 3.15 ساخته شده است. این برنامه به کاربران اجازه می‌دهد تا وظایفی را ایجاد کنند و پس از انجام آن‌ها، آن‌ها را از لیست حذف کنند.

## ویژگی‌ها

- **ایجاد وظیفه**: افزودن وظایف جدید به لیست کارها.
- **علامت‌گذاری به عنوان انجام‌شده**: حذف وظایف از لیست با علامت‌گذاری آن‌ها به عنوان انجام‌شده.
- **ایجاد حساب کاربری**: ایجاد حساب کاربری برای دیدن لیست کارها.
- **خروج از حساب کاربری**: خارح شدن از حساب کاربری.
- **ساخت توکن**: ایجاد توکن برای اعتبار سنجی کاربر.

## نصب و راه‌اندازی

1. مخزن را کلون کنید:

    ```bash
    git clone https://github.com/yourusername/todo.git
    cd todo
    ```

2. یک محیط مجازی ایجاد کنید:

    ```bash
    python -m venv venv
    source venv/bin/activate  # در ویندوز از `venv\Scripts\activate` استفاده کنید
    ```

3. بسته‌های مورد نیاز را نصب کنید:

    ```bash
    pip install -r requirements.txt
    ```

4. مایگریشن‌ها را اعمال کنید:

    ```bash
    python manage.py migrate
    ```

5. سرور توسعه را اجرا کنید:

    ```bash
    python manage.py runserver
    ```

## نقاط پایانی API

- **GET /**: دریافت لیستی از تمام وظایف.
- **POST /tasks/add_task/**: ایجاد یک وظیفه جدید.
- **DELETE /tasks/done/{id}/**: حذف یک وظیفه با استفاده از ID آن.
- **POST /accounts/register/**: ایجاد حساب کاربری.
- **POST /accounts/logout/**: خروج از حساب کاربری.

## نحوه استفاده

1. سرور را اجرا کنید:

    ```bash
    python manage.py runserver
    ```

2. برای دیدن لیست وظایف درخواست GET به `/` ارسال کنید.
3. مرورگر خود یا Postman را باز کنید و به آدرس `http://127.0.0.1:8000/` بروید تا با API تعامل کنید.

4. برای ایجاد یک وظیفه جدید، یک درخواست POST به `/tasks/add_task/` با جزئیات وظیفه در بدنه درخواست ارسال کنید.

5. برای علامت‌گذاری یک وظیفه به عنوان انجام‌شده، درخواست DELETE به `/tasks/done/{id}/` ارسال کنید.
6. برای ساخت حساب کاربری جدید درخواست POST به `/accounts/register/` ارسال کنید.
7. برای خروج از حساب کاربری درخواست POST به `/accounts/logout/` ارسال کنید.

## وابستگی‌ها

- Python 3.11
- Django 5.1
- Django REST Framework 3.15

## تماس

اگر سؤالی دارید یا پیشنهادی دارید، می‌توانید با من از طریق ایمیل [imanmozafari.neonse@gmail.com](mailto:imanmozafari.neonse@gmail.com) در تماس باشید.
