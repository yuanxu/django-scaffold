# Django 脚手架

# 表单验证

基于[FormValidation](http://formvalidation.io/)。

## 支持的验证

* [between](http://formvalidation.io/validators/between/)
* [callback](http://formvalidation.io/validators/callback/)
* [choice](http://formvalidation.io/validators/choice/)
* [date](http://formvalidation.io/validators/date/)
* [different](http://formvalidation.io/validators/different/)
* [emailAddress](http://formvalidation.io/validators/emailAddress/)
* [file](http://formvalidation.io/validators/file/) *可自动根据ImageFile，VideoFile设置校验类型*
* [greaterThan](http://formvalidation.io/validators/greaterThan/)
* [id](http://formvalidation.io/validators/id/)
* [identical](http://formvalidation.io/validators/identical/)
* [integer](http://formvalidation.io/validators/integer/)
* [lessThan](http://formvalidation.io/validators/lessThan/)
* [notEmpty](http://formvalidation.io/validators/notEmpty/)
* [numeric](http://formvalidation.io/validators/numeric/)
* [phone](http://formvalidation.io/validators/phone/)
* [regexp](http://formvalidation.io/validators/regexp/)
* [remote](http://formvalidation.io/validators/remote/)
* [stringLength)(http://formvalidation.io/validators/stringLength/)
* [uri](http://formvalidation.io/validators/uri/)
* [zipCode](http://formvalidation.io/validators/zipCode/)

## 用法

* 激活scaffold_toolkit.formvalidator

```#!python
INSTALLED_APPS=(
    ...
    scaffold_toolkit.formvalidator,
    ...
)
```

* 按照常规定义Django的model和form。定义时的验证规则，会自动生成客户端验证脚本。

*　验证脚本

在需要验证的模板上，根据情况，添加如下代码存根。

```#!html
{% load formvalidator %}
<link rel="stylesheet" href="{% formvalidator_css_url %}">

<script src="{% formvalidator_javascript_url %}">
<script src="{% formvalidator_language_url 'zh_CN' %}"> <!-- if needed -->
<script>
    {% formvalidator 'formSelector' form  %}
</script>
```

## 校验类

formvalidator已经原生支持Django的校验，比如不为空(notEmpty)，字符串长度(stringLength)等等。只需要按照Django的常规方法定义相关的字段即可。

对于部分特殊的校验，如phone、zip等，可以在form中设置校验类。在scaffold_toolkit.formvalidator.forms.validators中提供了一组自定义校验类:

* IdValidator
* ZipCodeValidator
* IdenticalValidator
* DifferentValidator
* RemoteValidator
* ChoicesValidator
* CallBackValidator
* PhoneValidator
* EmailAddressValidator
* UriValidator
* FileValidator
* ImageFileValidator
* VideoFileValidator
* AudioFileValidator


# zui表单工具

# Middleware

# mailgun

# widgets