# minidatabase

# English Introduction(当然也包括中文介绍)

A tiny database system based on python dictionary
# Minidb Python Third-Party Database



Minidb is a Python third-party database that provides a simple and easy-to-use interface for creating, appending and managing databases. It allows for database creation and manipulation without having to use any complex SQL commands.



## Installation



To install Minidb, you can use pip by running the following command:



```

pip install minidatabase

```



## Usage



To start using minidb, you must first import the library by using the following command:



``` python

from minidatabase import minidb

```



### Creating a Database



To create a local database, you can use the `connect` method, which takes a single parameter, the path to the database. For example:



``` python

db = minidb.connect('example.minidb')

```



To create a WebMDB server database, you can use the `web_connect` method, which takes three parameters: password, server_address and port. You can start the server using the `minidb -w` command on the command line. You can then create a database using the `minidb -c example.minidb` command.



### Database Operations



After creating a cursor for the database, you can start using the various database operations. Here are some important ones:



#### Append Method



The append method is used to add data to the database. It takes two parameters, `tag` and `value`, and is used to create a new tag and assign it a value. For example:



``` python

db.append('name', 'John')

```



#### Delete Method



The delete method is used to delete an entry from the database by tag name. For example:



``` python

db.delete('name')

```



#### Search Method



The search method is used to search the database for a keyword. It returns a list of tags with matching keywords. For example:



``` python

db.search('age')

```



#### Search_value Method



The search_value method is used to search the database for a specific value. It returns a list of tags with matching values. For example:



``` python

db.search_value('John')

```



#### Search_tag Method



The search_tag method is used to search the database for a specific tag. It returns a list of tags with matching tag names. For example:



``` python

db.search_tag('name')

```



#### Clean Method



The clean method is used to clear the database. For example:



``` python

db.clean()

```



#### List Method



The list method is used to list all the entries in the database. For example:



``` python

db.list()

```



#### Commit Method



The commit method is used to save the changes made to the database. For example:



``` python

db.commit()

```



#### Close Method



The close method is used to close the database cursor. For example:



``` python

db.close()

```



## Contributions



Minidb welcomes and appreciates any contributions. If you find any bugs or have any suggestions for improvement, feel free to create a pull request or an issue in the repository.



## License



This project is licensed under the  GNU GENERAL PUBLIC LICENSE - see the `LICENSE` file for details.

By HansenL ©2021-2023


# minidatabase 起源微数据库

# 中文介绍

一个基于Python字典的微型数据库系统

# Minidb Python第三方数据库

Minidb是一个Python第三方数据库，提供了一个简单易用的接口来创建、追加和管理数据库。它允许在不使用任何复杂的SQL命令的情况下创建和操作数据库。

## 安装

要安装Minidb，您可以使用pip运行以下命令：

```
pip install minidatabase
```

## 使用

要开始使用minidb，您必须首先使用以下命令导入库：
``` python
from minidatabase import minidb
```

### 创建数据库

要创建本地数据库，您可以使用connect方法，它需要一个参数，即数据库路径。例如：

```python
db = minidb.connect('example.minidb')
```

要创建WebMDB服务器数据库，您可以使用web_connect方法，它需要三个参数：密码、服务器地址和端口。您可以在命令行上使用minidb -w命令启动服务器。然后，您可以直接在终端使用

```
minidb -c example.minidb
```
命令创建一个数据库。

### 数据库操作
在为数据库创建游标之后，您可以开始使用各种数据库操作。以下是一些重要的操作：

#### 追加方法
追加方法用于向数据库添加数据。它需要两个参数：tag和value，用于创建一个新标签并为其分配一个值。例如：
``` python
db.append('name', 'John')
```

#### 删除方法
删除方法用于按标签名称从数据库中删除条目。例如：

``` python
db.delete('name')
```

#### 搜索方法
搜索方法用于在数据库中搜索关键字。它返回一个具有匹配关键字的标签列表。例如：

``` python
db.search('age')
```

#### Search_value方法

Search_value方法用于在数据库中搜索特定的值。它返回一个具有匹配值的标签列表。例如：
``` python
db.search_value('John')
```

#### Search_tag方法

Search_tag方法用于在数据库中搜索特定的标签。它返回一个具有匹配标签名称的标签列表。例如：

``` python
db.search_tag('name')
```

#### Clean方法

Clean方法用于清除数据库。例如：

``` python
db.clean()
```

#### List方法

List方法用于列出数据库中的所有条目。例如：

``` python
db.list()
```

#### Commit方法

Commit方法用于保存对数据库所做的更改。例如：

``` python
db.commit()
```

#### Close方法

Close方法用于关闭数据库游标。例如：

``` python
db.close()
```

## 贡献者们

Minidatabase欢迎并感谢任何贡献。如果您发现任何错误或有任何改进建议，请随时在存储库中创建拉取请求或问题。

## 许可证明细
本项目根据GNU GENERAL PUBLIC LICENSE许可证授权 - 有关详细信息，请参见“LICENSE”文件。

开发者 HansenL ©2021-2023
