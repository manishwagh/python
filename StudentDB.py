print 'Welcome to student mgnt'
while True:
    try:
        file_temp = open('student_db.txt', 'r')
    except IOError:
        print 'To run this program, you must have student_db.txt file in the same folder ...\n' \
               'This program is coded and developed by Choyon Ahmed'
        exit_prompt = input('Press enter/CTRL+C to close the window ...\n==> ')
    fetched_file = eval(file_temp.read())
    try:
        print 'Total Entries in database:', len(fetched_file.keys())
        command1 = raw_input('What you want me to do(type the number. ex. 1)?\n'
                             '1. Update Student Database\n'
                             '2. View Full Student Database\n'
                             '3. Find a Student by Roll Number\n==> ')
        if command1 == '1':
            command2 = raw_input('1. Add Student Data\n'
                                 '2. Delete Student Data\n'
                                 '3. Clear Full Database\n==> ')
            if command2 == '1':
                file_temp.close()
                file_edit_temp = open('student_db.txt', 'r')
                file_edit = eval(file_edit_temp.read())
                file_edit_temp.close()
                key1 = raw_input('Enter New Student Roll Number: \n==> ')
                print 'Enter Student data as asked :'
                student_name = '\tStudent Name: %r \n' % raw_input('Student Name:\n==> ')
                cgpa = '\tCGPA: %r \n' % float(raw_input('CGPA: \n==> '))
                credit_complete = '\tTotal Credit Completed: %r \n' % int(raw_input('Total Credit Completed: \n==> '))
                join_date = '\tDate of Registration: %r \n' % raw_input('Date of Registration: \n==> ')
                expiration_date = '\tSession ends: %r ' % raw_input('Session ends: \n==> ')
                create_value = student_name + cgpa + credit_complete + join_date + expiration_date
                file_edit[key1] = create_value
                file_edit_temp = open('student_db.txt', 'w')
                file_edit_temp.write('%r' % file_edit)
                file_edit_temp.close()
                print 'SYSTEM: Data Updated Successfully for student roll', key1
                # This portion is under development.
                continue
            elif command2 == '2':
                file_temp1 = open('student_db.txt', 'r')
                file_temp2 = eval(file_temp1.read())
                file_temp1.close()
                key_to_delete = raw_input('Enter Student Roll number to delete: \n==> ')
                try:
                    del file_temp2[key_to_delete]
                    file_temp1 = open('student_db.txt', 'w')
                    file_temp1.write('%r' % file_temp2)
                    file_temp1.close()
                    print 'Roll number', key_to_delete, 'Has been deleted successfully!'
                    continue
                except KeyError:
                    print 'ERROR: Student Roll Number is not assigned to the database!'
                    continue
            elif command2 == '3':
                print 'Are you sure want to clear the whole database?If you proceed, this action cannot be reverted ' \
                      'back!'
                delete_confirm = raw_input('Type Y to continue or N to abort the action\n==> ')
                if delete_confirm == 'Y':
                    file_temp.close()
                    file_temp = open('student_db.txt', 'w')
                    file_temp.write('{}')
                    file_temp.close()
                    print 'SYSTEM: Database cleared successfully!'
                    continue
                elif delete_confirm == 'N':
                    print 'SYSTEM: Action Aborted ...'
                    continue
                else:
                    print 'SYSTEM: Invalid Command!'
                    continue
            else:
                print 'ERROR: Invalid Command!'
                continue
        elif command1 == '2':
            checkme = len(fetched_file.keys())
            if checkme == 0:
                print 'SYSTEM: There is no student information stored in the database!'
                continue
            else:
                for key in fetched_file:
                    print 'Roll Number:', key
                    print fetched_file[key]
                continue
        elif command1 == '3':
            while True:
                find_student = raw_input('Type student roll number :\n==> ')
                try:
                    print 'Student Information: \n', fetched_file[find_student]
                    print '\tRoll number: %r' % find_student
                    # might be extended with something more here later
                except KeyError:
                    print 'ERROR: Roll number not found in the database'
                    continue
        else:
            print 'ERROR: Invalid Command!'
            continue
    except ValueError:
        print 'ERROR: Invalid Command!'
	continue
