/**
 * Created by cfit008 on 18/8/16.
 */

$(document).ready(function () {
    $('#btn_mod1').click(function () {
       var name=$('#ip1').val();
       var phone_no= $('#ip2').val();
       var email= $('#ip3').val();
       var street= $('#ip4').val();
       var city= $('#ip5').val();
       var state= $('#ip6').val();
       var pin_code= $('#ip7').val();

       if(name==''||phone_no==''){
           $('#msg_add').text('Phone number and name are required');}
       else if(phone_no.length!=10){
           $('#msg_add').text('Phone no should contain 10 digits');
                }
       else {

                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie !== '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                        }
                       }
                      }
                        return cookieValue;
                      }
                      var csrftoken = getCookie('csrftoken');

                      $.ajaxSetup({
                      beforeSend: function(xhr) {
                      if (!this.crossDomain) {
                      xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                       }
                      });


                    $.ajax({
                        type:'POST',
                        url:'modify_contact',
                        data: {name: name, phone_no:phone_no,email:email,street:street,city:city,state:state,pin_code:pin_code},
                        success:function (data) {
                            $('#msg_add').text(data)
                        }
                    });
                }

    });
});