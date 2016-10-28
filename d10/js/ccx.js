

/*
def Foo():
	pass
*/	

//name = 'ccx' 全局变量
//var name = 'ccx' 局部变量

/*
window.name = 'xxxxxx'
Foo()
Bar()
function Foo(name){
	//var arg2 = arguments[1]
	var name = 'ccx'
	console.log(name);
	//console.log(arg2);
}

function Bar(){
	console.log(name)
}

*/

//自执行函数
(function(name){
	console.log(name);
})('ccx')