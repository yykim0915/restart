use test

db.emp.find({}, {_id:0, eno:1, ename:1, sal:1})

db.emp.update(
	{sal:{$lt:2500}},
	{$inc: {sal:1000}},
	{multi:true}
)

db.emp.find({}, {_id:0, eno:1, ename:1, sal:1})
