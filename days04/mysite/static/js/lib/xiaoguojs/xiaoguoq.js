var fnTextPopup = function(arr, options) {
	// arr参数是必须的
	if(!arr || !arr.length) {
		return;
	}
	// 主逻辑
	var index = 0;
	document.documentElement.addEventListener('click', function(event) {
		var x = event.pageX,
			y = event.pageY;
		var eleText = document.createElement('span');
		eleText.className = 'text-popup';
		this.appendChild(eleText);
		if(arr[index]) {
			eleText.innerHTML = arr[index];
		} else {
			index = 0;
			eleText.innerHTML = arr[0];
		}
		// 动画结束后删除自己
		eleText.addEventListener('animationend', function() {
			eleText.parentNode.removeChild(eleText);
		});
		// 位置
		eleText.style.left = (x - eleText.clientWidth / 2) + 'px';
		eleText.style.top = (y - eleText.clientHeight) + 'px';
		// index递增
		index++;
	});
};

//fnTextPopup(['富强','❤', '民主','❤', '文明', '❤','和谐','❤', '自由', '❤','平等','❤', '公正','❤', '法治', '❤','爱国','❤', '敬业','❤', '诚信','❤', '友善','❤']);
fnTextPopup(['第一次见到你，我就知道我栽了。', '海底月是天上月，眼前人是心上人。', '越向往光明，越要默默地扎根于黑暗。','秒回的人应该很温柔吧，他不舍得让你等太久', '有人说，时间让人忘记疼，我不觉得。时间只能让人习惯疼','一缕阳光向眼眸倾泻，一丝微风对脸颊轻抚', ' 我的句子却到不了你们的心里', ' 他的幼稚，我的偏激，都活成了历史', 
'别让人笑话你的遭遇','强者自救，圣者渡人','你涉世未深，也让你与众不同', ' 一缕阳光向眼眸倾泻，一丝微风对脸颊轻抚',' 他的幼稚，我的偏激，都活成了历史']);