import os
import zipfile
import shutil
import time



def extract_submissions_zip(filename, extract_to):
    """Extract filename(submissions.zip) and put all 
    the contents inside the dst_dir."""
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def extract_zip_files(src_dir, dst_dir):
    '''Extract all .zip files from src_dir and put them in dst_dir.
    For instance, if there is a zip file as John_Doe.zip inside the src_dir,
    it will extract and put all the contents in *John_Doe* directory 
    inside the dst_dir.
    '''
    os.makedirs(dst_dir, exist_ok=True)
    for entry in os.listdir(src_dir):
        if entry.endswith('.zip'):
            zip_file_path = os.path.join(src_dir, entry)
            dirname = os.path.splitext(entry)[0]  # Remove .zip
            dirname = dirname.replace(' ', '_')  # Replace spaces with underscores
            extraction_path = os.path.join(dst_dir, dirname)

            os.makedirs(extraction_path, exist_ok=True)

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extraction_path)


def process_files(src_dir, dst_dir, dir_structure, file_extensions):
    """Copy source code files of file_extensions to a structured directory
    for each student."""
    os.makedirs(dst_dir, exist_ok=True)
    for entry in os.listdir(src_dir):
        entry_path = os.path.join(src_dir, entry)
        if os.path.isdir(entry_path):
            src_code_files = [f for f in find_src_code_files(entry_path, 
                                                             file_extensions)]
            processed_student_dir = os.path.join(dst_dir, entry, 
                                                 *dir_structure)
            os.makedirs(processed_student_dir, exist_ok=True)

            for file in src_code_files:
                shutil.copy(file, processed_student_dir)


def find_src_code_files(directory, file_extensions):
    """Search for files with the file extensions inside the directory
    and return the file paths as a generator."""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            _, file_extension = os.path.splitext(filename)
            if file_extension in file_extensions:
                yield os.path.join(dirpath, filename)



if __name__ == '__main__':
    print('Processing student submissions ...')

    # 
    # UPDATE THESE ACCORDINGLY
    #
    hw_name = 'HW1'
    dir_structure = ['edu', 'mystate', 'cs101', 'hw1']
    src_code_file_extensions = ['.java',]
    submissions_zip_filename = 'submissions.zip'


    project_root_dir = os.path.dirname(os.path.abspath(__file__))
    submissions_dir = os.path.join(project_root_dir, hw_name, 'submissions')
    submissions_unzipped_dir = os.path.join(project_root_dir, hw_name, 
                                            'submissions_unzipped')
    submissions_for_moss_dir = os.path.join(project_root_dir, hw_name, 
                                            'submissions_for_moss')


    submissions_zip_filepath = os.path.join(project_root_dir,
                                            submissions_zip_filename)
    extract_submissions_zip(submissions_zip_filepath, submissions_dir)
    time.sleep(1)
    extract_zip_files(submissions_dir, submissions_unzipped_dir)
    time.sleep(1)
    process_files(submissions_unzipped_dir, submissions_for_moss_dir,
                  dir_structure, src_code_file_extensions)

    print('All submissions have been processed for Moss. Ready to upload.')
