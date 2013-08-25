'use strict';

/* Directives */


angular.module('Flaskular.directives', [])
    .directive('appVersion', ['version', function(version) {
        return function(scope, elm, attrs) {
            elm.text(version);
        };
    }])
    .directive('navTabs', ['$location', function(location) {
        //Taken from http://plnkr.co/edit/xwGtGqrT7kWoCKnGDHYN?p=preview
        return {
            restrict: 'A',
            link: function(scope, element) {
                var $ul = $(element);

                //will be a map from the url the menuitem links to
                //back to the listitem. That way when the location
                //changes we can search this map to find the li that
                //should now be active.

                var tabMap = {};
                var $tabs = $ul.children();
                $tabs.each(function() {
                    var $li = $(this);
                    //Substring 1 to remove the # at the beginning
                    //(because location.path() below does not return
                    //the #)
                    var href = $li.find('a').attr('href');
                    if(href[0] == '#')
                        href = href.substring(1);
                    tabMap[href] = $li;
                });

                scope.location = location;
                scope.$watch('location.path()', function(newPath) {
                    $tabs.removeClass("active");
                    tabMap[newPath].addClass("active");
                });
            }
        };
    }]);
