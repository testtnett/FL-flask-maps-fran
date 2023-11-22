## dev
:heavy_check_mark: online via browser  
:heavy_check_mark: local via vscode remote  
:heavy_check_mark: open browser via vscode tunnel  
open browser online via docker ext : rightclick on ..  

reset / recreate DB:  
*flask reset*  



### debug
- [x] vscode launch config: Python: Flask
- [ ] flask python live reload  

#### flask < 2.2 :  
debug env parameter:  
*export FLASK_APP=app.py*  
*export FLASK_ENV=development*  
*flask run*  

:heavy_check_mark: works, compiles on save delayed < vscode settings > troubles with autosave ?  
debug.sh = shell script starts flask with debug params:  
*./debug.sh*  
set execute permission for current user:   
*chmod u+x debug.sh* 

#### flask 2.2  
*flask --app main.py --debug run*  
and env parameter works also

## live share
ok created mit vscode, share to tester in brave  
no commit for tester  
terminal bash: erstmal read only, request edit via bell = ok  


## codespace + team
devcontainer ,.. ins repo  
repo moved to team   
open as tester = :heavy_check_mark: ok lauft  
push from tester = :heavy_check_mark: ok  

## secrets
- [x] DB pwds 
- [x] api key

how to share ? = github codespace team secrets 

#### show env vars
echo $DATABASE_URL  
echo $POSTGRES_PASSWORD  
echo $PGADMIN_DEFAULT_PASSWORD  
echo $GOOGLE_MAPS_API_KEY  

## markdown
https://github.com/testtnett/notes/blob/main/doc/markdown.md