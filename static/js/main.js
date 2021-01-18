$(document).ready(function(){
	$('.datetimeinput').datepicker({changeYear: true, changeMonth: true,dateFormat:'yy-mm-dd'});
	$('.table-page').paging({limit:10,activePage:0});
	NProgress.start();
	NProgress.set(.5);
	NProgress.done();
	$('.toggle-btn').click(function(){
		$(this).parent('.search-box').css("left","0");
		if($(this).parent('.search-box').hasClass('out'))
		{

	  		$(this).parent().css("left","0");
	    	$(this).parent().toggleClass("out");
		}else{
	    	$(this).parent().css("left","-500px");
	      	$(this).parent().toggleClass("out");
	    }
	});

});