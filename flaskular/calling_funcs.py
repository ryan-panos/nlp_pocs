
import csv


def get_a_series_of_calls(input_file, service_ls, get_service_by_tag):

    # f = open(output_file, 'wt')
    input_path_file = "data/" + input_file
    vendor_response = []
    SEND_ONE_REPONSE = False

    try:
        # writer = csv.writer(f)

        with open(input_path_file, 'rU') as f: #@ rb
            reader = csv.reader(f, delimiter=',', quotechar='"')  #quoting=csv.QUOTE_NONE  dialect=csv.excel_tab
            # reader = csv.reader(f, delimiter=',', quotechar=csv.)  # quoting=csv.QUOTE_NONE
            content_idx=-1
            for idx, row in enumerate(reader):

                if idx == 0 and "content" in row:
                        # print " IS HEADER? " + str(row)
                        # print "content in " + str(row.index("content"))
                        content_idx = row.index("content")

                        # row.append(SUMY_COLUMN)
                        # writer.writerow(row)

                elif content_idx > -1:
                    # print "CONTENT: " + str(row[content_idx])


                    # sum_sentances = get_sumy_response(row[content_idx])
                    # row.append(sum_sentances)
                    # writer.writerow(row)
                    one_resp = {}
                    for service_str in service_ls:
                        print "----------service_str---------:" + service_str
                        one_resp[service_str]=get_service_by_tag(row[content_idx], service_str)
                        # this_content_services.append(one_resp)

                        # print "\n : Got one response: " + str(one_resp[service_str]) + "\n"
                    vendor_response.append(one_resp)

                else:
                    print "%% ERR: content column not detected - could it be marked differently?"
    except Exception as e:
        print 'The following exception occurred in config:'
        print str(e)
    finally:
        if len(vendor_response) > 0 and SEND_ONE_REPONSE:
            print "\n\n----------------\n RETURNING a list " + str(len(vendor_response)) + " long with members like: " + str(vendor_response[0])
        else:
            print "\n\n----------------\n RETURNING a list " + str(
                len(vendor_response)) + " long with members like: "  ## + str(vendor_response[0])

        return vendor_response


def get_all_vendor_responses(input_file, vendor_func):

    # f = open(output_file, 'wt')
    input_path_file = "data/" + input_file
    vendor_response = []

    try:
        # writer = csv.writer(f)

        with open(input_path_file, 'rU') as f: #@ rb
            reader = csv.reader(f, delimiter=',', quotechar='"')  #quoting=csv.QUOTE_NONE  dialect=csv.excel_tab
            # reader = csv.reader(f, delimiter=',', quotechar=csv.)  # quoting=csv.QUOTE_NONE
            content_idx=-1
            for idx, row in enumerate(reader):

                if idx == 0 and "content" in row:
                        # print " IS HEADER? " + str(row)
                        # print "content in " + str(row.index("content"))
                        content_idx = row.index("content")

                        # row.append(SUMY_COLUMN)
                        # writer.writerow(row)

                elif content_idx > -1:
                    # print "CONTENT: " + str(row[content_idx])
                    print "-------------------"

                    # sum_sentances = get_sumy_response(row[content_idx])
                    # row.append(sum_sentances)
                    # writer.writerow(row)

                    one_resp = vendor_func(row[content_idx])
                    # print "Got one response: " + str(one_resp)
                    vendor_response.append(one_resp)

                else:
                    print "%% ERR: content column not detected - could it be marked differently?"

    finally:
        print "RETURNING a list " + str(len(vendor_response)) + " long with members like: " + str(vendor_response[0])
        return vendor_response
        # f.close()

# def get_get_all_vendor_responses