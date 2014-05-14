STATIC_SCSS =	common/static/sass/bourbon

PUBLIC_CSS_VENDOR =	common/static/css/vendor/font-awesome.css

PUBLIC_FONTS_VENDOR =	common/static/fonts/vendor/fontawesome-webfont.eot \
			common/static/fonts/vendor/fontawesome-webfont.svg \
			common/static/fonts/vendor/fontawesome-webfont.ttf \
			common/static/fonts/vendor/fontawesome-webfont.woff

PUBLIC_IMAGES =	lms/static/images/follow-dog-ear.png \
			lms/static/images/moderator-edit-icon.png \
			lms/static/images/show-hide-discussion-icon.png \
			lms/static/images/vote-plus-icon.png \
			lms/static/images/moderator-delete-icon.png \
			lms/static/images/new-post-icons-full.png \
			common/static/images/spinner-on-grey.gif \
			lms/static/images/wmd-buttons-transparent.png

PUBLIC_JS_VENDOR =	common/static/js/vendor/mathjax-MathJax-c9db6ac \
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
			lms/static/js/split.js

PUBLIC_JS =	common/static/coffee/src/discussion/content.js \
		common/static/coffee/src/discussion/discussion_filter.js \
		common/static/coffee/src/discussion/discussion_module_view.js \
		common/static/coffee/src/discussion/main.js \
		common/static/coffee/src/discussion/templates.js \
		common/static/coffee/src/discussion/views \
		common/static/coffee/src/discussion/discussion.js \
		common/static/coffee/src/discussion/discussion_router.js \
		common/static/coffee/src/discussion/models

TEMPLATES_HTML =	lms/templates/discussion/_filter_dropdown.html

TEMPLATES_MUSTACHE =	lms/templates/discussion/mustache/_inline_discussion_cohorted.mustache \
			lms/templates/discussion/mustache/_inline_thread_show.mustache \
			lms/templates/discussion/mustache/_profile_thread.mustache \
			lms/templates/discussion/mustache/_inline_discussion.mustache \
			lms/templates/discussion/mustache/_pagination.mustache \
			lms/templates/discussion/mustache/_user_profile.mustache

.PHONY: $(STATIC_SCSS) $(PUBLIC_CSS_VENDOR) $(PUBLIC_FONTS_VENDOR) $(PUBLIC_IMAGES) \
	$(PUBLIC_JS_VENDOR) $(PUBLIC_JS) $(TEMPLATES_HTML) $(TEMPLATES_MUSTACHE) fix_deps

all:	$(STATIC_SCSS) $(PUBLIC_CSS_VENDOR) $(PUBLIC_FONTS_VENDOR) $(PUBLIC_IMAGES) \
	$(PUBLIC_JS_VENDOR) $(PUBLIC_JS) $(TEMPLATES_HTML) $(TEMPLATES_MUSTACHE) fix_deps

$(STATIC_SCSS):
	cp -r ${EDX}/$@ discussion_forum/static/scss

$(PUBLIC_CSS_VENDOR):
	cp ${EDX}/$@ discussion_forum/public/css/vendor

$(PUBLIC_FONTS_VENDOR):
	cp ${EDX}/$@ discussion_forum/public/fonts/vendor

$(PUBLIC_IMAGES):
	cp ${EDX}/$@ discussion_forum/public/images

$(PUBLIC_JS_VENDOR):
	cp -r ${EDX}/$@ discussion_forum/public/js/vendor

$(PUBLIC_JS):
	cp -rn ${EDX}/$@ discussion_forum/public/js

$(TEMPLATES_HTML):
	cp -r ${EDX}/$@ discussion_forum/templates/html

$(TEMPLATES_MUSTACHE):
	cp -r ${EDX}/$@ discussion_forum/templates/mustache

fix_deps:
	./fix_deps.sh
