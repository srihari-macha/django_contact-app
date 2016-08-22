/**
 * Created by cfit008 on 17/8/16.
 */

$(document).ready(function () {
    $('#del_btn').click(function () {
        var phone_no=$('#phone').val();
        if(phone_no.length==0){
            $('#msg_add').text('phone no required');
        }
        else if( phone_no.length!=10){
            $('#msg_add').text('invalid phone no!!');
        }

        else{

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
                      var csrftoken1 = getCookie('csrftoken');

                      $.ajaxSetup({
                      beforeSend: function(xhr) {
                      if (!this.crossDomain) {
                      xhr.setRequestHeader("X-CSRFToken", csrftoken1);
                        }
                       }
                      });


            $.ajax({
                type:'POST',
                url: 'delete_contact',
                data:{phone_no:phone_no},
                success:function (data) {
                    $('#msg_add').text(data);
                }
            });

        }
    });
});

