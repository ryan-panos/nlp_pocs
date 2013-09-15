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
            $log.info("Querying people");
            $scope.$log = $log;
            $log.info(Object.keys(Person.query({},function(result) {
                $scope.people = result.objects;
            })));
        }
    ]);
