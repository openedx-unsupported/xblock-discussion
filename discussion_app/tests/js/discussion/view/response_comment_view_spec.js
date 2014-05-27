// Generated by CoffeeScript 1.6.1
(function() {

  describe('ResponseCommentView', function() {
    var makeEventSpy;
    beforeEach(function() {
      window.$$course_id = 'edX/999/test';
      window.user = new DiscussionUser({
        id: '567'
      });
      DiscussionUtil.loadRoles([]);
      this.comment = new Comment({
        id: '01234567',
        user_id: user.id,
        course_id: $$course_id,
        body: 'this is a response',
        created_at: '2013-04-03T20:08:39Z',
        abuse_flaggers: ['123'],
        roles: ['Student']
      });
      setFixtures("<script id=\"response-comment-show-template\" type=\"text/template\">\n    <div id=\"response-comment-show-div\"/>\n</script>\n<script id=\"response-comment-edit-template\" type=\"text/template\">\n    <div id=\"response-comment-edit-div\">\n        <div class=\"edit-comment-body\"><textarea/></div>\n        <ul class=\"edit-comment-form-errors\"/>\n    </div>\n</script>\n<div id=\"response-comment-fixture\"/>");
      this.view = new ResponseCommentView({
        model: this.comment,
        el: $("#response-comment-fixture")
      });
      spyOn(ResponseCommentShowView.prototype, "convertMath");
      spyOn(DiscussionUtil, "makeWmdEditor");
      return this.view.render();
    });
    makeEventSpy = function() {
      return jasmine.createSpyObj('event', ['preventDefault', 'target']);
    };
    describe('_delete', function() {
      var setAjaxResult;
      beforeEach(function() {
        this.comment.updateInfo({
          ability: {
            can_delete: true
          }
        });
        this.event = makeEventSpy();
        spyOn(this.comment, "remove");
        return spyOn(this.view.$el, "remove");
      });
      setAjaxResult = function(isSuccess) {
        var _this = this;
        return spyOn($, "ajax").andCallFake(function(params) {
          (isSuccess ? params.success : params.error)({});
          return {
            always: function() {}
          };
        });
      };
      it('requires confirmation before deleting', function() {
        spyOn(window, "confirm").andReturn(false);
        setAjaxResult(true);
        this.view._delete(this.event);
        expect(window.confirm).toHaveBeenCalled();
        expect($.ajax).not.toHaveBeenCalled();
        return expect(this.comment.remove).not.toHaveBeenCalled();
      });
      it('removes the deleted comment object', function() {
        setAjaxResult(true);
        this.view._delete(this.event);
        expect(this.comment.remove).toHaveBeenCalled();
        return expect(this.view.$el.remove).toHaveBeenCalled();
      });
      it('calls the ajax comment deletion endpoint', function() {
        setAjaxResult(true);
        this.view._delete(this.event);
        expect(this.event.preventDefault).toHaveBeenCalled();
        expect($.ajax).toHaveBeenCalled();
        return expect($.ajax.mostRecentCall.args[0].url._parts.path).toEqual('/courses/edX/999/test/discussion/comments/01234567/delete');
      });
      it('handles ajax errors', function() {
        spyOn(DiscussionUtil, "discussionAlert");
        setAjaxResult(false);
        this.view._delete(this.event);
        expect(this.event.preventDefault).toHaveBeenCalled();
        expect($.ajax).toHaveBeenCalled();
        expect(this.comment.remove).not.toHaveBeenCalled();
        expect(this.view.$el.remove).not.toHaveBeenCalled();
        return expect(DiscussionUtil.discussionAlert).toHaveBeenCalled();
      });
      return it('does not delete a comment if the permission is false', function() {
        this.comment.updateInfo({
          ability: {
            'can_delete': false
          }
        });
        spyOn(window, "confirm");
        setAjaxResult(true);
        this.view._delete(this.event);
        expect(window.confirm).not.toHaveBeenCalled();
        expect($.ajax).not.toHaveBeenCalled();
        expect(this.comment.remove).not.toHaveBeenCalled();
        return expect(this.view.$el.remove).not.toHaveBeenCalled();
      });
    });
    describe('renderShowView', function() {
      return it('renders the show view, removes the edit view, and registers event handlers', function() {
        spyOn(this.view, "_delete");
        spyOn(this.view, "edit");
        this.view.renderEditView();
        this.view.renderShowView();
        this.view.showView.trigger("comment:_delete", makeEventSpy());
        expect(this.view._delete).toHaveBeenCalled();
        this.view.showView.trigger("comment:edit", makeEventSpy());
        expect(this.view.edit).toHaveBeenCalled();
        expect(this.view.$("#response-comment-show-div").length).toEqual(1);
        return expect(this.view.$("#response-comment-edit-div").length).toEqual(0);
      });
    });
    describe('renderEditView', function() {
      return it('renders the edit view, removes the show view, and registers event handlers', function() {
        spyOn(this.view, "update");
        spyOn(this.view, "cancelEdit");
        this.view.renderEditView();
        this.view.editView.trigger("comment:update", makeEventSpy());
        expect(this.view.update).toHaveBeenCalled();
        this.view.editView.trigger("comment:cancel_edit", makeEventSpy());
        expect(this.view.cancelEdit).toHaveBeenCalled();
        expect(this.view.$("#response-comment-show-div").length).toEqual(0);
        return expect(this.view.$("#response-comment-edit-div").length).toEqual(1);
      });
    });
    describe('edit', function() {
      return it('triggers the appropriate event and switches to the edit view', function() {
        var editTarget;
        spyOn(this.view, 'renderEditView');
        editTarget = jasmine.createSpy();
        this.view.bind("comment:edit", editTarget);
        this.view.edit();
        expect(this.view.renderEditView).toHaveBeenCalled();
        return expect(editTarget).toHaveBeenCalled();
      });
    });
    return describe('with edit view displayed', function() {
      beforeEach(function() {
        return this.view.renderEditView();
      });
      describe('cancelEdit', function() {
        return it('triggers the appropriate event and switches to the show view', function() {
          var cancelEditTarget;
          spyOn(this.view, 'renderShowView');
          cancelEditTarget = jasmine.createSpy();
          this.view.bind("comment:cancel_edit", cancelEditTarget);
          this.view.cancelEdit();
          expect(this.view.renderShowView).toHaveBeenCalled();
          return expect(cancelEditTarget).toHaveBeenCalled();
        });
      });
      return describe('update', function() {
        beforeEach(function() {
          var _this = this;
          this.updatedBody = "updated body";
          this.view.$el.find(".edit-comment-body textarea").val(this.updatedBody);
          spyOn(this.view, 'cancelEdit');
          return spyOn($, "ajax").andCallFake(function(params) {
            if (_this.ajaxSucceed) {
              params.success();
            } else {
              params.error({
                status: 500
              });
            }
            return {
              always: function() {}
            };
          });
        });
        it('calls the update endpoint correctly and displays the show view on success', function() {
          this.ajaxSucceed = true;
          this.view.update(makeEventSpy());
          expect($.ajax).toHaveBeenCalled();
          expect($.ajax.mostRecentCall.args[0].url._parts.path).toEqual('/courses/edX/999/test/discussion/comments/01234567/update');
          expect($.ajax.mostRecentCall.args[0].data.body).toEqual(this.updatedBody);
          expect(this.view.model.get("body")).toEqual(this.updatedBody);
          return expect(this.view.cancelEdit).toHaveBeenCalled();
        });
        return it('handles AJAX errors', function() {
          var originalBody;
          originalBody = this.comment.get("body");
          this.ajaxSucceed = false;
          this.view.update(makeEventSpy());
          expect($.ajax).toHaveBeenCalled();
          expect($.ajax.mostRecentCall.args[0].url._parts.path).toEqual('/courses/edX/999/test/discussion/comments/01234567/update');
          expect($.ajax.mostRecentCall.args[0].data.body).toEqual(this.updatedBody);
          expect(this.view.model.get("body")).toEqual(originalBody);
          expect(this.view.cancelEdit).not.toHaveBeenCalled();
          return expect(this.view.$(".edit-comment-form-errors *").length).toEqual(1);
        });
      });
    });
  });

}).call(this);