.. _mongodb:


***************
mongodb
***************

基本命令
=============================

document database: data -> js objects

js语法::

  for(i=0; i<10; i++) { print('hello'); }; 

save **document** {a: 99} to **collection** scores:: 

  db.scores.save({a: 99}); 
  db.scores.find(); 

shell一次只显示10条结果， ``it`` 可以显示下一批

查找all documents where a == 2::

  db.scores.find({a: 2}); 

查找documents where a > 15::

  db.scores.find({a: {'$gt': 15}}); 

* $lt  - '<',   $lte - '<=', 
* $gte - '>=',  $ne  - '!='
* $in - 'is in array',  $nin - '! in array'

修改name为johnny的整个document::

  db.users.update({name: 'Johnny'}, {name: 'Cash', languages: ['english']}); 

部分更改::

  db.users.update({name: 'Cash'}, {'$set': {'age': 50} }); 

push and pull items from arrays::

  db.users.update({name: 'Sue'}, {'$pull': {'languages': 'scala'} }); 
  db.users.update({name: 'Sue'}, {'$push': {'languages': 'ruby'} }); 

删除符合条件的documents::

  db.users.remove({name: 'Sue'});

delete everything from a collection::

  db.scores.remove();

例子
=============================

命令行::

	$ mongo
	  MongoDB shell version: 2.0.0
	  connecting to: test
	  > use example
	  switched to db example
	  > show dbs
	  > db.movies.insert({title: "The Matrix", year: 1999});
	  > db.movies.insert({title: "Star Wars", year: 1977});
	  > db.movies.find();
	  { "_id" : ObjectId("4e7018a79abdbdfb5d235b6c"), "title" : "The Matrix", "year" : 1999 }
	  { "_id" : ObjectId("4e7018dd9abdbdfb5d235b6d"), "title" : "Star Wars", "year" : 1977 }
	  > quit()
