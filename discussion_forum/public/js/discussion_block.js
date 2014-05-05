// TODO HACK: not set in the LMS
 var $$course_id = "edX/Open_DemoX/edx_demo_course";//"{{course_id|escape}}";

function DiscussionBlock(runtime, element) {
  var el = $(element).find('.discussion-module');
  new DiscussionModuleView({
    el: el
  });
}
