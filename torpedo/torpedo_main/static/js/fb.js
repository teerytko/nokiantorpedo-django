define(['facebook'], function(){
  var channelUrl = '//'+HTTP_HOST+'/channel';
  FB.init({
    appId      : '205098582998927',
    channelUrl : channelUrl,
    status     : true,
    xfbml      : true  
  });
  FB.getLoginStatus(function(response) {
    console.log(response);
  });
});