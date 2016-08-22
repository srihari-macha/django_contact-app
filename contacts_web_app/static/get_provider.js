/**
 * Created by cfit008 on 18/8/16.
 */

$(document).ready(function () {
    $('#btn_pro').click(function () {
            var phone_no=$('#phone').val();

            if(phone_no.length==0){
                $('#msg_add').text('please enter mobile no')
            }
            else if(phone_no.length!=10){
                $('#msg_add').text('phone no contain 10 digits')
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
                    url:'get_provider',
                    data:{phone_no:phone_no},
                    success:function (data) {

                        $('#msg_add').text(data)
                    }

                });
            }
    });
});
