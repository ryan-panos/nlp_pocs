'use strict';

/* Controllers */

angular.module('Flaskular.controllers', [])
    .controller('HomeCtrl', [
        function() { }])
    .controller('ContactCtrl', [
        function() { }])
    .controller('FourOhFourCtrl', [
        function() { }]);

console.log(" LOADING!!! IbmCtrl!! ");

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

angular.module('Flaskular.controllers', ['Flaskular.services'])
    .controller('IbmCtrl', ['$scope', '$log', 'TestIBMService',
        function ($scope, $log, TestIBMService) {

            var update = function () {
                TestIBMService.query({}, function(result) {

                    console.log(" >> GOT BACK: ", result);

                    $scope.big_res = result;
                    $scope.orginal_text = result["orginal_text"];

                    console.log(" >> $scope.big_res: ", $scope.big_res);
                });
            };

            $log.info("testing IBM!");


            $scope.test_str = " Annnnd DOING IBM ! ";
            update();

            // $scope.save = function() {
            //     $log.info("Adding: ", $scope.search);
            //     var newper = new Person({'name': $scope.search});
            //     newper.$save();
            //     update();
            // };
        }
                              ]);

console.log("> DID  LOADING!!! IbmCtrl!! ");