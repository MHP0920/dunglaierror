# Phát hiện Dũng Lại Lập Trình - Lỗi cơ bản

## Thư viện được lập trình để giúp người mới nhập môn lập trình khi học khóa cơ bản của Dũng Lại Lập Trình có thể sửa lỗi, tiếp thu thông tin dễ hơn.

## Documentation

### Setup
> pip install dunglaierrors

*hoặc*

> pip install git+https://github.com/MHP0920/dunglaierror.git

*hoặc*

> git clone https://github.com/MHP0920/dunglaierror.git

> cd dunglaierror

> python setup.py install

### Usage

#### Khởi động thư viện

```py
import dunglaierrors
dunglaierrors.init()
```

#### Class tài liệu

```py
documents = dunglaierrors.Docs()
```

Tài liệu về chuyển đổi tiền tệ

```py
documents.doitiente()
```

Tài liệu về if else statement

```py
documents.ifelse()
```

Tài liệu về "AI if else"

```py
documents.fakeAI()
```

Tài liệu về keylogger

```py
documents.keylogger()
```

#### Kiểm tra mã

Class kiểm tra

```py
checker = dunglaierrors.Check()
```

Kiểm tra mã đổi USD sang VND

```py
checker.usdtovnd(code_or_path)
```

Kiểm tra mã "AI"

```py
checker.fakeAI(code_or_path)
```

### License
> __MIT LICENSE__

### Copyright

Copyright @ **MHP** 2022. All rights reserved.
