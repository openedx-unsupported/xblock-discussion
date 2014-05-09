 var $$course_id = "{{course_id}}";

function DiscussionBlock(runtime, element) {
  var el = $(element).find('.discussion-module');

  /* We check if the block is used with jquery.xblock.
   * TODO Maybe we could extend the jquery.xblock runtime to have a getLmsBaseUrl?
   */
  var testUrl = runtime.handlerUrl(element, 'test');
  if (testUrl.match(/^(http|https):\/\//)) {
    var hostname = testUrl.match(/^(.*:\/\/[a-z\-.]+)\//)[1];
    DiscussionUtil.setBaseUrl(hostname);
  }

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