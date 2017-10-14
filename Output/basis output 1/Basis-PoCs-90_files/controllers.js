'use strict';

/* Controllers */

angular.module('nlpPOCs.controllers', [])
    .controller('HomeCtrl', [
        function() { }])
    .controller('ContactCtrl', [
        function() { }])
    .controller('FourOhFourCtrl', [
        function() { }]);

console.log(" LOADING!!! IbmCtrl!! ");

angular.module('nlpPOCs.controllers', ['nlpPOCs.services'])
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

angular.module('nlpPOCs.controllers', ['nlpPOCs.services'])
    .controller('IbmCtrl', ['$scope', '$log', 'TestIBMService',
        function ($scope, $log, TestIBMService) {
            $scope.ALL = "All";
            $scope.MANY = "Many";
            $scope.TARGET = "TARGET";
            $scope.OTHER = "Other";
            $scope.selectedMode = $scope.MANY;

            $scope.modes = [$scope.ALL, $scope.MANY,  $scope.OTHER];  //$scope.TARGET,

            $scope.DEFAULT_FILE = '<short default file>';
            $scope.ENV_FILE_10 = 'dataset_934_env_short.csv';
            $scope.ENV_FILE_1238 = 'dataset_840_env1.csv';
            $scope.TEST_NLP = 'test_nlp.csv';
            $scope.selectedFile = $scope.DEFAULT_FILE;

            $scope.inputFiles = [$scope.DEFAULT_FILE, $scope.ENV_FILE_10, $scope.ENV_FILE_1238, $scope.TEST_NLP];

            $scope.hiddenSources = [];  //  probably need to initiate min length

            $scope.IBM = "IBM";
            $scope.BASIS = "Basis";
            $scope.vendorOptions = [$scope.IBM, $scope.BASIS];
            $scope.selectedVendor = $scope.BASIS;

            console.log("INIT-ish selectedMode: ", $scope.selectedMode);

            $scope.hideSource = function (idx) {
                $scope.hiddenSources[idx] = true;
            };

            $scope.showSource = function (idx) {
                $scope.hiddenSources[idx] = undefined;
            };

            $scope.onModeChange = function () {
                console.log("onModeChange selectedMode: ", $scope.selectedMode);
                updatePage();
            };

            $scope.onReLoad = function () {
                updatePage();
            }

            $scope.onFileChange = function () {
                console.log("onFileChange selectedFile: ", $scope.selectedFile);
                updatePage();
            };

            $scope.onVendorChange = function () {
                console.log("-- onVendorChange selectedVendor: ", $scope.selectedVendor);
                if ($scope.selectedVendor == $scope.BASIS) {
                    $scope.selectedMode = $scope.MANY;
                    $scope.mode_str = "No All mode for Basis (that we know of) so doing many . . ..";
                }
                updatePage();
            };

            var updatePage = function() {

                if ($scope.selectedFile == $scope.DEFAULT_FILE) {
                    $scope.sentInputFile = '';
                } else {
                    $scope.sentInputFile = $scope.selectedFile;
                }

                if (!$scope.selectedMode || $scope.selectedMode == $scope.ALL ) {
                    $scope.mode_str = " Annnnd DOING Allll of " + $scope.selectedVendor + " at once!! ";
                    $scope.loading_status = 'Calling ' + $scope.selectedVendor + ' . ..';
                    //.<img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getAll();
                } else if ($scope.selectedMode == $scope.MANY) {
                    $scope.mode_str = " Annnnd DOING " + $scope.selectedVendor + " in chunks ! ";
                    $scope.loading_status = 'Calling ' + $scope.selectedVendor + ' . ...';
                    // <img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getMany();
                } else if ($scope.selectedMode == $scope.TARGET) {
                    $scope.mode_str = " Annnnd DOING the " + $scope.selectedVendor + " services we are targeting ! ";
                    $scope.loading_status = 'Calling ' + $scope.selectedVendor + ' . ...';
                    // <img class="blinking-cursor" src="static/img/blinking-cursor.gif-c200"/>
                    getMany();//todo !!!
                }
            };
            var getAll = function () {

                // TODO: maybe remove last?

                TestIBMService.queryAll({input_file: $scope.sentInputFile, selected_vendor: $scope.selectedVendor}, function(result) {

                    console.log(" >> GOT BACK: ", result);

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    if (result["selected_vendor"]) {
                        $scope.selected_vendor = result["selected_vendor"];
                    }

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                });
            };

            var getMany = function () {

                // TODO: maybe remove last?

                TestIBMService.queryMany({selected_vendor: $scope.selectedVendor, input_file: $scope.sentInputFile}, function(result) {

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    if (result["selected_vendor"]) {
                        $scope.selected_vendor = result["selected_vendor"];
                    }

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                    // console.log(" >> $scope.big_res[0]: ", $scope.big_res_ls[0]);
                });
            };

            var getTarget = function () {
                TestIBMService.queryTarget({selected_vendor: $scope.selectedVendor, input_file: $scope.sentInputFile}, function(result) {

                    console.log(" >> GOT BACK: ", result);

                    $scope.big_res_ls = result;
                    $scope.loading_status = "";
                    if (result["selected_vendor"]) {
                        $scope.selected_vendor = result["selected_vendor"];
                    }

                    console.log(" >> $scope.big_res: ", $scope.big_res_ls);
                });
            };


            $log.info("testing IBM! (this is init like . ...) ");
            updatePage()

        }
                              ]);

console.log("> DID  LOADING!!! IbmCtrl!! ");