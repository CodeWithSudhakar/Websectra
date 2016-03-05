$(document).ready(function(){

//Navbar
$("#fixednav").wrap('<div class="nav-placeholder"></div>');
$(".nav-placeholder").height($("#fixednav").outerHeight());


var navoffset=$("#fixednav").offset().top;
var lastscroll=0;
$(window).scroll(function(){
var scrollpos=$(window).scrollTop();
if(scrollpos>=navoffset){								//scroll more than logo
$("#fixednav").addClass("fixed");
$("#sidenav").addClass("fixed-left");
$("#content").addClass("offset-s2");
}
else{													//scroll less than logo
$("#fixednav").removeClass("fixed");
$("#sidenav").removeClass("fixed-left");
$("#sidenav").removeClass("fixed-left-below");
$("#content").removeClass("offset-s2");
}

if(scrollpos<lastscroll){								//scroll up
$("#fixednav").addClass("fixed-below");
$("#logo").addClass("fixed");
$("body").addClass("scrollup");
$("#sidenav").addClass("fixed-left-below");
$("#content").addClass("offset-s2");
}
else{													//scroll down
$("#fixednav").removeClass("fixed-below");
$("#logo").removeClass("fixed");
$("body").removeClass("scrollup");
$("#sidenav").removeClass("fixed-left-below");
}
lastscroll=scrollpos;
});


//Initialising dropbox
	$('.dropdown-button').dropdown({
      inDuration: 0,
      outDuration: 0,
      constrain_width: true, // Does not change width of dropdown to that of the activator
      hover: false, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true // Displays dropdown below the button
    }
  );

  
//Initialising select
$('select').material_select();


 //Initialising modal
$('.modal-trigger').leanModal();


//On Clicking logo
$("#logoname").onClick(function(){
$("#body").addClass("scrollup");
});

//Initializing Select
    $('select').material_select();	
      

//dropbox hover
$( "#drop" ).hover(
  function() {
    $( this ).addClass( "grey" );
  }, function() {
    $( this ).removeClass( "grey" );
  }
);

});

