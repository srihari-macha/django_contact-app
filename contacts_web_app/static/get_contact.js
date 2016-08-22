/**
 * Created by cfit008 on 17/8/16.
 */

$(document).ready(function () {
    $('#get_cnt_btn').click(function () {

         var phone_no=$('#phone').val();

    if(phone_no==''||phone_no.length!=10){
        $('#msg_add').text('invalid phone number !!!');

    }
    else {
        $.ajax({
            type:'POST',
            url:'get_contact',

            success:function (data) {
                $('#msg_add').text(data)
            }
        });

    }

    });


});