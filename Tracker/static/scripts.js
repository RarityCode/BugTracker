
function AddOption(tag, value) {
	var select = document.getElementById(tag);
	var option = document.createElement('option');
	option.value = value;
	option.text = value;
	select.add(option);
}






