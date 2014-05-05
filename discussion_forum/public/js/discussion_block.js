// TODO HACK: not set in the LMS
 var $$course_id = "edX/Open_DemoX/edx_demo_course";//"{{course_id|escape}}";

function DiscussionBlock(runtime, element) {
  var el = $(element).find('.discussion-module');
  new DiscussionModuleView({
    el: el
  });
}

function DiscussionBlockEditor(runtime, element) {
    $('.xblock-save-button').bind('click', function() {
        var data = {
            'display_name': $('#display-name').val(),
            'discussion_category': $('#discussion-category').val(),
            'discussion_target': $('#discussion-target').val(),
        };
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        $.post(handlerUrl, JSON.stringify(data)).complete(function() {
            window.location.reload(false);
        });
    });
}