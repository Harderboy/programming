var d1 = new Date("October 13, 1975 11:13:00")
var d2=new Date()
// getTime() 返回从 1970 年 1 月 1 日至今的毫秒数。
console.log(d2.getTime())
console.log(d2.toLocaleString())
console.log(d2.toLocaleTimeString())
console.log(d2.toLocaleDateString())

console.log(d2-d1)

var myDate=new Date()
console.log(myDate)
myDate.setDate(myDate.getDate()+5)
console.log(myDate)

var myDate2=new Date(1619667537000)
console.log(myDate2)

// windows是全局对象（顶层对象）
console.log(window.document)
console.log(window.location)
console.log(window.history)

function func(){
	console.log("点我干啥？")
	// window.location.href="red.html"
	// window.location.reload(true)
	// window.location.assign(url) ： 加载 URL 指定的新的 HTML 文档。 就相当于一个链接，跳转到指定的url，当前页面会转为新页面内容，可以点击后退返回上一个页面。
	window.location.assign("red.html")
	
}

function func1(){
	// html 超链接标签 href 属性 target="_blank" 的作用是使打开的链接以新开的窗口形式出现。
	window.open("red.html","blank","width=200px,height=400px,top=0,left=20px");
}

function func2(){
	// Scripts may close only the windows that were opened by them. 非弹出窗口，即是指（opener=null及非window.open()打开的窗口）。
	window.close()
}
function func3(){
	// html 超链接标签 href 属性 target="_blank" 的作用是使打开的链接以新开的窗口形式出现。
	window.open("blue.html","blank","width=200px,height=400px,top=0,left=20px");
}