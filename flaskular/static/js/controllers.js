'use strict';

/* Controllers */

angular.module('Flaskular.controllers', [])
    .controller('HomeCtrl', [
        function() { }])
    .controller('ContactCtrl', [
        function() { }])
    .controller('FourOhFourCtrl', [
        function() { }]);


angular.module('Flaskular.controllers', ['Flaskular.services'])
    .controller('PeopleCtrl', ['$scope', '$log', 'Person',
        function ($scope, $log, Person) {
            var update = function () {
                Person.query({}, function(result) {
                    $scope.people = result.objects;
                });
            };

            $log.info("Querying people");
            update();

            $scope.save = function() {
                $log.info("Adding: ", $scope.search);
                var newper = new Person({'name': $scope.search});
                newper.$save();
                update();
            };
        }
                              ]);
