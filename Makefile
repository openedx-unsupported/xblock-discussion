STATIC_CSS =	lms/static/sass/discussion-app.css

STATIC_CSS_VENDOR =	common/static/css/vendor/font-awesome.css

STATIC_FONTS_VENDOR =	common/static/fonts/vendor/fontawesome-webfont.eot \
			common/static/fonts/vendor/fontawesome-webfont.svg \
			common/static/fonts/vendor/fontawesome-webfont.ttf \
			common/static/fonts/vendor/fontawesome-webfont.woff

STATIC_IMAGES =	lms/static/images/follow-dog-ear.png \
			lms/static/images/moderator-edit-icon.png \
			lms/static/images/show-hide-discussion-icon.png \
			lms/static/images/vote-plus-icon.png \
			lms/static/images/moderator-delete-icon.png \
			lms/static/images/new-post-icons-full.png \
			common/static/images/spinner-on-grey.gif \
			lms/static/images/wmd-buttons-transparent.png

STATIC_JS_VENDOR =	common/static/js/vendor/mathjax-MathJax-c9db6ac \
			lms/static/js/mustache.js \
			common/static/js/vendor/backbone-min.js \
			common/static/js/vendor/jquery.leanModal.min.js \
			common/static/js/vendor/underscore-min.js \
			common/static/js/vendor/jquery.timeago.js \
			lms/static/js/Markdown.Editor.js \
			lms/static/js/Markdown.Sanitizer.js \
			lms/static/js/Markdown.Converter.js \
			common/static/js/vendor/URI.min.js \
			common/static/js/test/i18n.js \
			lms/static/coffee/src/mathjax_delay_renderer.js \
			lms/static/js/split.js \
			lms/static/coffee/src/customwmd.js

STATIC_DISCUSSION_JS =	common/static/coffee/src/discussion/content.js \
		common/static/coffee/src/discussion/discussion_filter.js \
		common/static/coffee/src/discussion/discussion_module_view.js \
		common/static/coffee/src/discussion/main.js \
		common/static/coffee/src/discussion/templates.js \
		common/static/coffee/src/discussion/views \
		common/static/coffee/src/discussion/discussion.js \
		common/static/coffee/src/discussion/discussion_router.js \
		common/static/coffee/src/discussion/models \
		common/static/coffee/src/discussion/utils.js \
		common/static/coffee/src/discussion/tooltip_manager.js

TEMPLATES_DISCUSSION_HTML =	lms/templates/discussion/_underscore_templates.html \
				lms/templates/discussion/_filter_dropdown.html \
				lms/templates/discussion/mustache \
				lms/templates/discussion/_thread_list_template.html

TEMPLATES_DISCUSSION_DISABLED_HTML =	lms/templates/discussion/_blank_slate.html \
					lms/templates/discussion/_discussion_course_navigation.html \
					lms/templates/discussion/_discussion_module.html \
					lms/templates/discussion/_discussion_module_studio.html \
					lms/templates/discussion/_inline_new_post.html \
					lms/templates/discussion/_js_body_dependencies.html \
					lms/templates/discussion/_js_data.html \
					lms/templates/discussion/_js_head_dependencies.html \
					lms/templates/discussion/_new_post.html \
					lms/templates/discussion/_paginator.html \
					lms/templates/discussion/_recent_active_posts.html \
					lms/templates/discussion/_search_bar.html \
					lms/templates/discussion/_similar_posts.html \
					lms/templates/discussion/_sort.html \
					lms/templates/discussion/_user_profile.html \
					lms/templates/discussion/index.html \
					lms/templates/discussion/maintenance.html \
					lms/templates/discussion/user_profile.html

TESTS =	common/static/coffee/spec/discussion

.PHONY: $(STATIC_CSS) $(STATIC_CSS_VENDOR) $(STATIC_FONTS_VENDOR) $(STATIC_IMAGES) \
	$(STATIC_JS_VENDOR) $(STATIC_DISCUSSION_JS) $(TEMPLATES_HTML) \
	$(TEMPLATES_DISCUSSION_DISABLED_HTML) $(TEMPLATES_DISCUSSION_HTML) $(TESTS) fix_deps

all:	$(STATIC_CSS) $(STATIC_CSS_VENDOR) $(STATIC_FONTS_VENDOR) $(STATIC_IMAGES) \
	$(STATIC_JS_VENDOR) $(STATIC_DISCUSSION_JS) $(STATIC_DISCUSSION_JS) $(TEMPLATES_HTML) \
	$(TEMPLATES_DISCUSSION_DISABLED_HTML) $(TEMPLATES_DISCUSSION_HTML) $(TESTS) fix_deps

$(STATIC_CSS):
	cp ${EDX}/$@ discussion_app/static/discussion/css

$(STATIC_CSS_VENDOR):
	cp ${EDX}/$@ discussion_app/static/discussion/css/vendor

$(STATIC_FONTS_VENDOR):
	cp ${EDX}/$@ discussion_app/static/discussion/fonts/vendor

$(STATIC_IMAGES):
	cp ${EDX}/$@ discussion_app/static/discussion/images

$(STATIC_JS_VENDOR):
	cp -r ${EDX}/$@ discussion_app/static/discussion/js/vendor

$(STATIC_DISCUSSION_JS):
	cp -r ${EDX}/$@ discussion_app/static/discussion/js

$(TEMPLATES_HTML):
	cp -r ${EDX}/$@ discussion_app/templates

$(TEMPLATES_DISCUSSION_HTML):
	cp -r ${EDX}/$@ discussion_app/templates/discussion

$(TEMPLATES_DISCUSSION_DISABLED_HTML):
	cp -r ${EDX}/$@ discussion_app/templates/discussion/disabled

$(TESTS):
	cp -r ${EDX}/$@ discussion_app/tests/js

fix_deps:
	./fix_deps.sh
