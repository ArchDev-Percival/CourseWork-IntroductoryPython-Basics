from string import digits
import os
def rename_files():

    Source_Directory = r"E:\Python\Level 0\prank";
    #List_all_files_and_folders_in_a_given_directory
    list_of_files = os.listdir(Source_Directory)
    print (list_of_files)

    #Python_3_has_a_different_implementation_of_str.translate_Check_out:"http://stackoverflow.com/questions/12851791/removing-numbers-from-string"
    remove_digits = str.maketrans("","",digits)
    #Use_Of_Type_Function
    print(type(remove_digits))

    #Current_Working_Directory_-_This_is_where_the_program_"RenameFiles.py"_is_located
    print(os.getcwd())
    #The_current_working_directory_is_being_changed_to_where_the_files_are_located
    os.chdir(Source_Directory)


    #For_each_file_in_the_folder_-_Since_we_are_changing_the_current_directory
    for file_name in list_of_files:
        os.rename(file_name,file_name.translate(remove_digits))
        if (file_name != file_name.translate(remove_digits)):
            print(file_name + " converted to " + file_name.translate(remove_digits))
        elif (file_name == file_name.translate(remove_digits)):
            print (file_name + " doesn't require to be converted")
    #@CommentedCode_below_would_require_the_fully_qualified_names_of_the_file.
                  ##If_while_renaming_the_full_path_was_left_out_and_only_the_filenames_provided_it_will_result_in_movement_of_the_files_to_the_current_directory
    #@CommentedCodefor file_name in list_of_files:
        #@CommentedCodeos.rename(r"E:\Python\Level 0\prank\\" + file_name,r"E:\Python\Level 0\prank\\"+file_name.translate(remove_digits))
        
rename_files()
