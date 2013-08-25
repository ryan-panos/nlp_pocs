'use strict';

/* Directives */


angular.module('Flaskular.directives', [])
  .directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }])
  .directive('navTabs', ['$location', function(location) {
    return {
        restrict: 'A',
        link: function(scope, element) {
            var $ul = $(element);

            var tabMap = {};
            var $tabs = $ul.children();
            $tabs.each(function() {
              var $li = $(this);
              //Substring 1 to remove the # at the beginning (because location.path() below does not return the #)
              tabMap[$li.find('a').attr('href').substring(1)] = $li;
            });

            scope.location = location;
            scope.$watch('location.path()', function(newPath) {
                $tabs.removeClass("active");
                tabMap[newPath].addClass("active");
            });
        }

    };

 }]);
