$(document).ready(function()
{
			$('#push').hide();	
			$('#loading').hide();		
			
			function validateForm()
			{
				
				var regex_sides =  /^[0-9]+$/;
				if($('#sides').val() == "" || parseInt($('#sides').val()) == 0 || parseInt($('#sides').val()) > 999999999 || !regex_sides.test( $('#sides').val() ) ) 
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
        	



				$('input#sides').on('click change',function(){
					validateForm()
					$('#result').empty()
					


				});
			
				$('#push').on('click',function(){ 
					$('#loading').show();
					$('#push').hide();
					});	


				$('result').on('click change',function(){
					if ( $('#result') == '' ){
						$('#loading').hide();
						
					}

				});
			});