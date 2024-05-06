% Open the file for writing
fileID = fopen('example.txt', 'w');
% Write some text to the file
fprintf(fileID, 'This is line 1\n');
fprintf(fileID, 'This is line 2\n');
fprintf(fileID, 'This is line 3\n');
% Close the file
fclose(fileID);

