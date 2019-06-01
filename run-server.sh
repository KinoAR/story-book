# To check server script running on port: lsof -t -i :8083 
nohup gunicorn -b :8083 story:app > nohup-story-book.out &
