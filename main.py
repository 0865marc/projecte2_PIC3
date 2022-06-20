from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from printer_log import Printer_log, Base

engine = create_engine('sqlite:///test.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") 


@app.get(path="/home.html", response_class=HTMLResponse)
async def home_page(request: Request):

    printer_log_table = []
    ## Printer_log_table = [
    #                   {printer_id, date, time, temperature, humidity, status},
    #                   {printer_id, date, time, temperature, humidity, status},
    #                   {printer_id, date, time, temperature, humidity, status},
    #                   etc...
    #                   ]

    unique_printer_id_list = session.query(Printer_log.printer_id).distinct().all()  # Return a list with every unique printer id [(101), (102), (103), etc..]
    for unique_id in unique_printer_id_list:
        # For every unique printer_id, get it's last log. (invert the list and take the first)
        printer_log = session.query(Printer_log).filter_by(printer_id=unique_id[0]).order_by(Printer_log.id.desc()).first()
        printer_log_table.append(printer_log.create_dict())
    
    
    return templates.TemplateResponse("home.html", {"request": request, "printer_log_table": printer_log_table})

@app.get(path="/historic_data.html", response_class=HTMLResponse)
async def historical_data(request: Request):
    printers_logs_table = []
    ## Printer_logs_table = [
    #                       [{printer_id, date, time, temperature, humidity, status},{""},{""},{""},{""},{""},{""},{""},{""},{""}]    last 10 logs of printer n1
    #                       [{printer_id, date, time, temperature, humidity, status},{""},{""},{""},{""},{""},{""},{""},{""},{""}]    last 10 logs of printer n2
    #                       [{printer_id, date, time, temperature, humidity, status},{""},{""},{""},{""},{""},{""},{""},{""},{""}]    last 10 logs of printer n3
    #                       etc
    #                       ]


    # Return a list with every unique printer id [(101), (102), (103), etc..]
    unique_printer_id_list = session.query(Printer_log.printer_id).distinct().all()  
    
    for unique_id in unique_printer_id_list:
        # For every unique printer_id, get it's last 10 logs. (invert the list and take the first 10)
        printer_last10logs = session.query(Printer_log).filter_by(printer_id=unique_id[0]).order_by(Printer_log.id.desc()).limit(10).all()

        printer_logs_dict = []
        for log in printer_last10logs:
            printer_logs_dict.append(log.create_dict())
            
        printers_logs_table.append(printer_logs_dict)
        print(printer_logs_dict)
        
    return templates.TemplateResponse("historic_data.html", {"request": request, "printer_logs_table": printers_logs_table})

if __name__ == "__main__":
    uvicorn.run(app)