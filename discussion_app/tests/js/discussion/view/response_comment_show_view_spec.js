// Generated by CoffeeScript 1.6.1
(function() {

  describe('ResponseCommentShowView', function() {
    beforeEach(function() {
      setFixtures("<ol class=\"responses\"></ol>\n<script id=\"response-comment-show-template\" type=\"text/template\">\n    <div id=\"comment_<%- id %>\">\n    <div class=\"response-body\"><%- body %></div>\n    <div class=\"discussion-flag-abuse notflagged\" data-role=\"thread-flag\" data-tooltip=\"report misuse\">\n    <i class=\"icon\"></i><span class=\"flag-label\"></span></div>\n    <div style=\"display:none\" class=\"discussion-delete-comment action-delete\" data-role=\"comment-delete\" data-tooltip=\"Delete Comment\" role=\"button\" aria-pressed=\"false\" tabindex=\"0\">\n      <i class=\"icon icon-remove\"></i><span class=\"sr delete-label\">Delete Comment</span></div>\n    <div style=\"display:none\" class=\"discussion-edit-comment action-edit\" data-tooltip=\"Edit Comment\" role=\"button\" tabindex=\"0\">\n      <i class=\"icon icon-pencil\"></i><span class=\"sr\">Edit Comment</span></div>\n    <p class=\"posted-details\">&ndash;posted <span class=\"timeago\" title=\"<%- created_at %>\"><%- created_at %></span> by\n    <% if (obj.username) { %>\n    <a href=\"<%- user_url %>\" class=\"profile-link\"><%- username %></a>\n    <% } else {print('anonymous');} %>\n    </p>\n    </div>\n</script>");
      this.comment = new Comment({
        id: '01234567',
        user_id: '567',
        course_id: 'edX/999/test',
        body: 'this is a response',
        created_at: '2013-04-03T20:08:39Z',
        abuse_flaggers: ['123'],
        roles: []
      });
      this.view = new ResponseCommentShowView({
        model: this.comment
      });
      return spyOn(this.view, "convertMath");
    });
    it('defines the tag', function() {
      expect($('#jasmine-fixtures')).toExist;
      expect(this.view.tagName).toBeDefined;
      return expect(this.view.el.tagName.toLowerCase()).toBe('li');
    });
    it('is tied to the model', function() {
      return expect(this.view.model).toBeDefined();
    });
    describe('rendering', function() {
      beforeEach(function() {
        spyOn(this.view, 'renderAttrs');
        return spyOn(this.view, 'markAsStaff');
      });
      it('produces the correct HTML', function() {
        this.view.render();
        return expect(this.view.el.innerHTML).toContain('"discussion-flag-abuse notflagged"');
      });
      it('can be flagged for abuse', function() {
        this.comment.flagAbuse();
        return expect(this.comment.get('abuse_flaggers')).toEqual(['123', '567']);
      });
      return it('can be unflagged for abuse', function() {
        var temp_array;
        temp_array = [];
        temp_array.push(window.user.get('id'));
        this.comment.set("abuse_flaggers", temp_array);
        this.comment.unflagAbuse();
        return expect(this.comment.get('abuse_flaggers')).toEqual([]);
      });
    });
    describe('_delete', function() {
      it('triggers on the correct events', function() {
        DiscussionUtil.loadRoles([]);
        this.comment.updateInfo({
          ability: {
            'can_delete': true
          }
        });
        this.view.render();
        return DiscussionViewSpecHelper.checkButtonEvents(this.view, "_delete", ".action-delete");
      });
      return it('triggers the delete event', function() {
        var triggerTarget;
        triggerTarget = jasmine.createSpy();
        this.view.bind("comment:_delete", triggerTarget);
        this.view._delete();
        return expect(triggerTarget).toHaveBeenCalled();
      });
    });
    return describe('edit', function() {
      it('triggers on the correct events', function() {
        DiscussionUtil.loadRoles([]);
        this.comment.updateInfo({
          ability: {
            'can_edit': true
          }
        });
        this.view.render();
        return DiscussionViewSpecHelper.checkButtonEvents(this.view, "edit", ".action-edit");
      });
      return it('triggers comment:edit when the edit button is clicked', function() {
        var triggerTarget;
        triggerTarget = jasmine.createSpy();
        this.view.bind("comment:edit", triggerTarget);
        this.view.edit();
        return expect(triggerTarget).toHaveBeenCalled();
      });
    });
  });

}).call(this);
