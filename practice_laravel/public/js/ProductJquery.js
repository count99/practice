$(document).ready(function(){
	var Quantity = +$("#values").val();
	var Price = +$("#price").val();

	$("#ProductPlus").click(function(){
		Quantity = Quantity + 1 ;
		$("#values").val(Quantity);
		$("#price").text(Price * Quantity);
	});

	$("#ProductMinus").click(function(){
		if(Quantity>1){
		Quantity = Quantity - 1 ;
		}
		$("#values").val(Quantity);
		$("#price").text(Price * Quantity);
	});
});
