# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.menu = []
    response.title = "Banner Security"
    return dict()

@auth.requires_membership('BannerSec')
def secmanager():
    groupie = auth.user_groups
    response.menu = [
        (T('Requests'), True, URL('default', 'secmanager'), []),
        (T('Classes (FSU Banner Security Manager Only)'), True, URL('default', 'classmanager'), []),
    ]
    response.title = "Banner Security"
    for key, value in groupie.items():
        if 'bannersec-adm' in value:
            message = 'Admin'
            admGrid = SQLFORM.grid(sqldb.admrequest, fields=(sqldb.admrequest.requesttype, sqldb.admrequest.first, sqldb.admrequest.last, sqldb.admrequest.requestdate, sqldb.admrequest.managerapprove, sqldb.admrequest.finalapprove, sqldb.admrequest.approver), onupdate=admGridUpdate)
            return dict(grid=admGrid, groupie=value, message=message)
        if 'bannersec-alu' in value:
            message = 'Alumni'
            aluGrid = SQLFORM.grid(sqldb.alurequest, fields=(sqldb.alurequest.requesttype, sqldb.alurequest.first, sqldb.alurequest.last, sqldb.alurequest.requestdate, sqldb.alurequest.managerapprove, sqldb.alurequest.finalapprove, sqldb.alurequest.approver), onupdate=aluGridUpdate)
            return dict(grid=aluGrid, groupie=value, message=message)
        if 'bannersec-fa' in value:
            message = 'Financial Aid'
            faGrid = SQLFORM.grid(sqldb.farequest, fields=(sqldb.farequest.requesttype, sqldb.farequest.first, sqldb.farequest.last, sqldb.farequest.requestdate, sqldb.farequest.managerapprove, sqldb.farequest.finalapprove, sqldb.farequest.approver), onupdate=faGridUpdate)
            return dict(grid=faGrid, groupie=value, message=message)
        if 'bannersec-fbo' in value:
            message = 'Financial Business Office'
            fboGrid = SQLFORM.grid(sqldb.fborequest, fields=(sqldb.fborequest.requesttype, sqldb.fborequest.first, sqldb.fborequest.last, sqldb.fborequest.requestdate, sqldb.fborequest.managerapprove, sqldb.fborequest.finalapprove, sqldb.fborequest.approver), onupdate=fboGridUpdate)
            return dict(grid=fboGrid, groupie=value, message=message)
        if 'bannersec-fcu' in value:
            message = 'Finance Campus Users'
            fcuGrid = SQLFORM.grid(sqldb.fcurequest, fields=(sqldb.fcurequest.requesttype, sqldb.fcurequest.first, sqldb.fcurequest.last, sqldb.fcurequest.requestdate, sqldb.fcurequest.managerapprove, sqldb.fcurequest.finalapprove, sqldb.fcurequest.approver), onupdate=fcuGridUpdate)
            return dict(grid=fcuGrid, groupie=value, message=message)
        if 'bannersec-hrp' in value:
            message = 'Human Resources / Pay'
            hrpGrid = SQLFORM.grid(sqldb.hrprequest, fields=(sqldb.hrprequest.requesttype, sqldb.hrprequest.first, sqldb.hrprequest.last, sqldb.hrprequest.requestdate, sqldb.hrprequest.managerapprove, sqldb.hrprequest.finalapprove, sqldb.hrprequest.approver), onupdate=hrpGridUpdate)
            return dict(grid=hrpGrid, groupie=value, message=message)
        if 'bannersec-it' in value:
            message = 'ITTS'
            itGrid = SQLFORM.grid(sqldb.ittsrequest, fields=(sqldb.ittsrequest.requesttype, sqldb.ittsrequest.first, sqldb.ittsrequest.last, sqldb.ittsrequest.requestdate, sqldb.ittsrequest.managerapprove, sqldb.ittsrequest.finalapprove, sqldb.ittsrequest.approver), onupdate=itGridUpdate)
            return dict(grid=itGrid, groupie=value, message=message)
        if 'bannersec-reg' in value:
            message = 'Registar'
            regGrid = SQLFORM.grid(sqldb.regrequest, fields=(sqldb.regrequest.requesttype, sqldb.regrequest.first, sqldb.regrequest.last, sqldb.regrequest.requestdate, sqldb.regrequest.managerapprove, sqldb.regrequest.finalapprove, sqldb.regrequest.approver), onupdate=regGridUpdate)
            return dict(grid=regGrid, groupie=value, message=message)
        if 'bannersec-sa' in value:
            message = 'Student Affairs'
            saGrid = SQLFORM.grid(sqldb.sarequest, fields=(sqldb.sarequest.requesttype, sqldb.sarequest.first, sqldb.sarequest.last, sqldb.sarequest.requestdate, sqldb.sarequest.managerapprove, sqldb.sarequest.finalapprove, sqldb.sarequest.approver), onupdate=saGridUpdate)
            return dict(grid=saGrid, groupie=value, message=message)
    else:
        message = "I'm sorry you are not a designated security manager for anything"
        return dict(message = message)

def admGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment + "\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def aluGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +                    
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def faGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def fboGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +                    
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def fcuGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n" +
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def hrpGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n" +
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
def itGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
        
def regGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )
    
def saGridUpdate(form):
    if form.vars.finalapprove == True:
        userMail = mail.send(to=[form.vars.banneruser + "@uncfsu.edu", form.vars.manageruser + "@uncfsu.edu"], subject='Banner Account Request - Approved', message=form.vars.banneruser +" " +"Your Banner Account Request has been approved.")
        secMail = mail.send(to=["ajohnson@uncfsu.edu", "jreed@uncfsu.edu"], subject="Pending Banner Security Class Request from ITTS", message="Request Information for" + " "+ form.vars.banneruser+"\n\n" +
        "May you grant my request to update my access to the following: "+ "\n" +
        "Security Classes:" + form.vars.securityclass + "\n \n" +
        "Request Type: " + form.vars.requesttype + "\n" +
        "First: " + form.vars.first + "\n" +
        "Middle Initial: "+ form.vars.middle + "\n" +
        "Last: " + form.vars.last + "\n" +
        "Department: " + form.vars.dept + "\n" +
        "Banner ID: " + form.vars.banner + "\n" +
        "Phone: " + form.vars.phone + "\n" +
        "Banner User: " + form.vars.banneruser + "\n" +
        "Effective Date: " + form.vars.effectivedate + "\n" +
        "Manager: " + form.vars.manageruser + "\n" +
        "Requested By: " + form.vars.requestedby + "@uncfsu.edu" + "\n"+
        "Manager Comments: " + form.vars.managercomment +"\n"+"\n\n"
        "This workorder was automatically generated by the Banner User Account Request application."
        )

@auth.requires_membership('bannersec-mgr')
def classmanager():
    response.menu = [
        (T('Requests'), True, URL('default', 'secmanager'), []),
        (T('Classes (FSU Banner Security Manager Only)'), True, URL('default', 'classmanager'), []),
    ]
    response.title = "Banner Security"
    manageGrid = SQLFORM.grid(sqldb.securityclass, fields=(sqldb.securityclass.dept, sqldb.securityclass.secclass, sqldb.securityclass.active, sqldb.securityclass.propername))
    return dict(grid=manageGrid)

@auth.requires_login()
def requestinit():
    response.menu = []
    response.title = "Banner Security"
    deptQuery = deptdb.executesql("SELECT description, deptID FROM [FSUcampus].[dbo].[dir_departments] ORDER BY description")
    admissions = sqldb((sqldb.securityclass.dept=="Admissions") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    alumni = sqldb((sqldb.securityclass.dept=="Alumni / Advancement") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    financecampus = sqldb((sqldb.securityclass.dept=="Finance Campus Users") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    financebusiness = sqldb((sqldb.securityclass.dept=="Finance for Business Office") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    finaid = sqldb((sqldb.securityclass.dept=="Financial Aid") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    hr = sqldb((sqldb.securityclass.dept=="Human Resources / Payroll") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    itts = sqldb((sqldb.securityclass.dept=="ITTS") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    registrar = sqldb((sqldb.securityclass.dept=="Registrar") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    studentaffairs = sqldb((sqldb.securityclass.dept=="Student Affairs") & (sqldb.securityclass.active==True)).select(sqldb.securityclass.ALL, orderby=sqldb.securityclass.secclass)
    return dict(depts=deptQuery, adm=admissions, alm=alumni, fc=financecampus, fb=financebusiness, fa=finaid, hr=hr, it=itts, reg=registrar, sa=studentaffairs)

@auth.requires_login()
def processinit():
    response.menu = []
    response.title = "Banner Security"
    if request.vars:
        if not request.vars.username == request.vars.manager:
            adm = []
            alu = []
            fcu = []
            fbo = []
            fa = []
            hr = []
            itts = []
            reg = []
            sa = []
            securityclasses = []
            if not request.vars.admission == None:
                if not type(request.vars.admission) is str:
                    for x in request.vars.admission:
                        adm.append(x)
                else:
                    adm.append(request.vars.admission)
                admStr = "|".join(adm)
                admID = sqldb.admrequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=admStr)
                admEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/adm/" + str(admID) + " to approve this request.")
            if not request.vars.alumni == None:
                if not type(request.vars.alumni) is str:
                    for x in request.vars.alumni:
                        alu.append(x)
                else:
                    alu.append(request.vars.alumni)
                aluStr = "|".join(alu)
                aluID = sqldb.alurequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=aluStr)
                aluEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/alu/" + str(aluID) + " to approve this request.")
            if not request.vars.financecampus == None:
                if not type(request.vars.financecampus) is str:
                    for x in request.vars.financecampus:
                        fcu.append(x)
                else:
                    fcu.append(request.vars.financecampus)
                fcuStr = "|".join(fcu)
                fcuID = sqldb.fcurequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=fcuStr, fundcode=request.vars.fundcode)
                fcuEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/fcu/" + str(fcuID) + " to approve this request.")
            if not request.vars.financebusiness == None:
                if not type(request.vars.financebusiness) is str:
                    for x in request.vars.financebusiness:
                        fbo.append(x)
                else:
                    fbo.append(request.vars.financebusiness)
                fboStr = "|".join(fbo)
                fboID = sqldb.fborequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=fboStr)
                fboEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/fcu/" + str(fboID) + " to approve this request.")
            if not request.vars.finaid == None:
                if not type(request.vars.finaid) is str:
                    for x in request.vars.finaid:
                        fa.append(x)
                else:
                    fa.append(request.vars.finaid)
                faStr = "|".join(fa)
                faID = sqldb.farequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=faStr)
                faEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/fa/" + str(faID) + " to approve this request.")
            if not request.vars.humanresources == None:
                if not type(request.vars.humanresources) is str:
                    for x in request.vars.humanresources:
                        hr.append(x)
                else:
                    hr.append(request.vars.humanresources)
                hrStr = "|".join(hr)
                hrID = sqldb.hrrequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=hrStr)
                hrEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/hr/" + str(hrID) + " to approve this request.")
            if not request.vars.itts == None:
                if not type(request.vars.itts) is str:
                    for x in request.vars.itts:
                        itts.append(x)
                else:
                    itts.append(request.vars.itts)
                ittsStr = "|".join(itts)
                ittsID = sqldb.ittsrequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=ittsStr)
                ittsEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/itts/" + str(ittsID) + " to approve this request.")
            if not request.vars.registrar == None:
                if not type(request.vars.registrar) is str:
                    for x in request.vars.registrar:
                        reg.append(x)
                else:
                    reg.append(request.vars.registrar)
                regStr = "|".join(reg)
                regID = sqldb.regrequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=regStr)
                regEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/reg/" + str(regID) + " to approve this request.")
            if not request.vars.studentaffairs == None:
                if not type(request.vars.studentaffairs) is str:
                    for x in request.vars.studentaffairs:
                        sa.append(x)
                else:
                    sa.append(request.vars.studentaffairs)
                saStr = "|".join(sa)
                saID = sqldb.sarequest.insert(requesttype=request.vars.requesttype, first=request.vars.first, middle=request.vars.middle, last=request.vars.last, dept=request.vars.department, banner=request.vars.banner, phone=request.vars.officephone, banneruser=request.vars.username, effectivedate=request.vars.effectivedate, manageruser=request.vars.manager, requestedby=auth.user.username, securityclass=saStr)
                saEmail = mail.send(to=[request.vars.manager + "@uncfsu.edu"], subject='Banner Account Request - Pending Manager Approval', message="You have a pending Banner Account Request from " + request.vars.first + " " + request.vars.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/manager/sa/" + str(saID) + " to approve this request.")
            message = "Your request has been emailed to your manager for approval, it will then be forwarded to the applicable Banner Security Managers."
        else:
            message = "Manager and Requester usernames must be different.  Please go back and try again."
    else:
            message = "Nothing to process."
    return dict(message=message)

@auth.requires_login()
def manager():
    response.menu = []
    response.title = "Banner Security"
    if request.args[0] == "adm":
        record = sqldb.admrequest[request.args[1]]
    if request.args[0] == "alu":
        record = sqldb.alurequest[request.args[1]]
    if request.args[0] == "fcu":
        record = sqldb.fcurequest[request.args[1]]
    if request.args[0] == "fbo":
        record = sqldb.fborequest[request.args[1]]
    if request.args[0] == "fa":
        record = sqldb.farequest[request.args[1]]
    if request.args[0] == "hr":
        record = sqldb.hrrequest[request.args[1]]
    if request.args[0] == "itts":
        record = sqldb.ittsrequest[request.args[1]]
    if request.args[0] == "reg":
        record = sqldb.regrequest[request.args[1]]
    if request.args[0] == "sa":
        record = sqldb.sarequest[request.args[1]]
    return dict(row=record)

@auth.requires_login()
def processmanager():
    response.menu = []
    depts = []
    den = ['den']
    if request.vars:
        if request.args[0] == "adm":
            record = sqldb.admrequest[request.args[1]]
            depts.append('Admissions')
        elif request.args[0] == "alu":
            record = sqldb.alurequest[request.args[1]]
            depts.append('Alumni / Advancement')
        elif request.args[0] == "fcu":
            record = sqldb.fcurequest[request.args[1]]
            depts.append('Finance Campus Users')
        elif request.args[0] == "fbo":
            record = sqldb.fborequest[request.args[1]]
            depts.append('Finance for Business Office')
        elif request.args[0] == "fa":
            record = sqldb.farequest[request.args[1]]
            depts.append('Financial Aid')
        elif request.args[0] == "hr":
            record = sqldb.hrrequest[request.args[1]]
            depts.append('Human Resources / Payroll')
        elif request.args[0] == "itts":
            record = sqldb.ittsrequest[request.args[1]]
            depts.append('ITTS')
        elif request.args[0] == "reg":
            record = sqldb.regrequest[request.args[1]]
            depts.append('Registrar')
        elif request.args[0] == "sa":
            record = sqldb.sarequest[request.args[1]]
            depts.append('Student Affairs')
        else:
            record = sqldb.admrequest[request.args[1]]
            depts.append('ERROR')
        if request.vars.decision == "approve":
            record.update_record(managerapprove=True, managercomment=request.vars.comments)
            if "Admissions" in depts:
                status = mail.send(to=["bannersec-adm@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Alumni / Advancement" in depts:
                status = mail.send(to=["bannersec-alu@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Finance Campus Users" in depts:
                status = mail.send(to=["bannersec-fcu@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Finance for Business Office" in depts:
                status = mail.send(to=["bannersec-fbo@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Financial Aid" in depts:
                status = mail.send(to=["bannersec-fa@uncfsu.edu","rtolenti@broncos.uncfsu.edu","ccampbell@uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Human Resources / Payroll" in depts:
                status = mail.send(to=["bannersec-hrp@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "ITTS" in depts:
                status = mail.send(to=["bannersec-it@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Registrar" in depts:
                status = mail.send(to=["bannersec-reg@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            if "Student Affairs" in depts:
                status = mail.send(to=["bannersec-sa@uncfsu.edu","rtolenti@broncos.uncfsu.edu"], subject='Banner Account Request - Pending Security Manager Approval', message="You have a pending Banner Account Request from " + record.first + " " + record.last + ".  Please go to https://app.uncfsu.edu/bannersec/default/secmanager to approve this request.")
            message = "You have approved this request.  An email will be sent to the corresponding Banner Security Managers for action."
        else:
            record.update_record(managerapprove=False, managercomment=request.vars.comments)
            message = "You have denied this request. An email will be sent to the corresponding Banner Security Manager to inform them of this action."
    else:
            message = "An error has occured.  The session probably expired, please go to the link in the notification email and try again."
    return dict(message=message,depts=depts)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()