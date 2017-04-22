$(document).ready(function()
{
			
			function validateForm()
			{
				var regex_sides =  /^[0-9]+$/;
				
				if($('#sides').val() == "" || parseInt($('#sides').val()) == 0 || parseInt($('#sides').val()) > 8800 || !regex_sides.test( $('#sides').val() ) ) 
				{
					$('#message').html('<b>Warning! \" '+ $('#sides').val() +' \" is not a valid sides !!<b>');
					$('#message').show();
					$('#push').hide();
					console.log(parseInt($('#sides').val()))
					
				}
				else{
					$('#message').hide();
					$('#push').show();
					}
			};
        	



				$('input#sides').on('click change',validateForm);
			
				$('#push').on('click',function(){ 
					validateForm();
					
					});	
			});