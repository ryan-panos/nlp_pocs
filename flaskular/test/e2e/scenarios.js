'use strict';

/* http://docs.angularjs.org/guide/dev_guide.e2e-testing */

describe('my app', function() {

  beforeEach(function() {
    browser().navigateTo('/');
  });



  describe('about', function() {

    beforeEach(function() {
      browser().navigateTo('/about');
    });


    it('should render about when user navigates to /about', function() {
      expect(element('[ng-view] h3:first').text()).
        toMatch(/About Flaskular/);
    });
    it('should have the about tab selected.', function() {
        expect(element('.navbar-nav li.active a[href="/about"]').count()).toEqual(1);
    });

  });


  describe('contact', function() {

    beforeEach(function() {
      browser().navigateTo('/contact');
    });


    it('should render contact when user navigates to /contact', function() {
      expect(element('[ng-view] h3:first').text()).
        toMatch(/Contact us/);
    });

    it('should have the contact tab selected.', function() {
        expect(element('.navbar-nav li.active a[href="/contact"]').count()).toEqual(1);
    });
  });

  describe('404', function() {
      it('should render the 404 partial with the right status', function() {
          browser().navigateTo('/404-not-exist');
          expect(browser().window().path()).toEqual('/404');
          //not sure how to ensure the status code yet.
          expect(element('[ng-view] h3:first').text()).toMatch(/404/);
      });
  });
});
