import requests
import os
from colorama import Fore , init
import time
init()
os.system("cls" or "clear")
clear = lambda: os.system('cls' or "clear")

var1=0
var2=0
var3 = 0
php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']

cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']

js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js']

cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']

brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']
strong = ['admin/','admin.asp/','admin/admin.asp/','admin.aspx/','admin/admin.aspx/','admin.php/','administrator/','login.php','admin.php','user/','usuarios/','usuario/','Admin/','cpanel/',
'phpmyadmin/','dashboard','cms/','users/','wp-login.php/','admin/login','auth/login/','moderator/','webadmin/','webmaster/','adminarea/','bb-admin/','wp-admin/','wp-login/'
,'wp-admin.php','userlogin/','logins/','login.html','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','panel/','forum/admin,adm/','cp/',
'vue-element-admin','admin/cp.php','cp.php','admincontrol/','admincp/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin_area/admin.php','admin_area/login.php'
,'siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','dashboard.html','dashboard.php'
,'bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp'
,'admincp/index.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html'
,'administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php',
'admin_area/admin.html','pages/admin/','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','members/,bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html'
,'admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html',
'controlpanel.php','admincontrol.php','admin/adminLogin.html','adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php'
,'webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html'
,'administrator/account.html','administrator.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html'
,'modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html,adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html'
,'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php'
,'panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php'
,'usuarios/login.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','admin.','login.','login1.','panel.','admin1.','admin2.','admin3.','admin4.'
,'moderator.','webadmin.','user.','administration/','mag/admin/','joomla/administrator/','manager/','adminpanel/','controlpanel/','logon/','auth/','apanel/','a/','acart/','access/','account/'
,'achievo/','address/','admins/','0admin/','admin1/','admin0','admin2/','admin3/','admin4/','admin5/','_adm_/','_admin_/','_administrator_/','_adm/','_admin/','achtung/','_administrator/'
,'AdminWeb/','administration.php','links/login.php','cms/_admin/logon.php','typo3/','pma/','cms/login/','access.php','sysadm.php','adm2/','include/admin.php','admin/moderator.php','interactive/admin.php'
,'edit.php','siteadmin/','hcaadmin.php','/svn/','blog/wp-login.php','admin/log.php','login/login.php','adminka.php','wholesale-login.php','authorize.php','editor/','base/admin/','includes/login.php'
,'site_admin/login.php','statredir/','lists/admin/','sec/login.php','bitrix/admin/','admin_tool/','cabinet/','klarnetCMS/','debug/rus/autorisation/','cms/admin/','Admin/private/','site/admin/','admen/'
,'admin2/index/','db/admin.php','admin/adm.php','admin/admin/','manager/ispmgr/','phpMyAdmin/','login.aspx/','admin/login.asp','admin/login.aspx/','moderator/admin.asp/','webadmin.asp/'
,'webadmin/admin.asp/','author/Admin.aspx/','admin/userAdmin.aspx/','dbadmin/','AdministratorS/Admin.aspx/','admin/secure/admin.aspx/','bb-admin/admin.asp/','processlogin.php/','0manager/','manager'
,'acceso.asp/','acceso.aspx/','account.asp/','account.aspx/','wp-login.asp/','wp-login.aspx/','admin_login/','admin-login/','modelsearch/','nsw/,rcjakar/','private.php/','_vti_pvt/','_private/'
,'admin1.php','admin2.html','yonetim.php','yonetim.html','nedmin/production/login.php','nedmin/production/index.php','yonetici.php','yonetici.html','admin1.asp','admin2.asp','yonetim.asp','yonetici.asp'
,'admin/index.asp','admin/home.asp','admin/controlpanel.asp','sysadmin.php','sysadmin.html','sysadmin/','ur-admin.asp','ur-admin.php','ur-admin.html','ur-admin/','administr8.php','administr8.html'
,'administr8/','admin/acceso.php/','admin/acceso.asp/','admin/acceso.aspx/','admin_area/acceso.php/','admin_area/acceso.asp/','admin_area/acceso.aspx/','adminarea/acceso.php/','adminarea/acceso.asp/'
,'adminarea/acceso.aspx/','admincontrol/acceso.php/','admincontrol/acceso.asp/','admincontrol/acceso.aspx/','admincpacceso.php/','admincpacceso.asp/','admincpacceso.aspx/','administrator/acceso.php/'
,'administrator/acceso.asp/','administrator/acceso.aspx/','admin_login/acceso.php/','admin_login/acceso.asp/','admin_login/acceso.aspx/','adminlogin/acceso.php/','adminlogin/acceso.asp/','adminlogin/acceso.aspx/'
,'webadmin/wp-login.php/','webadmin/wp-login.asp/','webadmin/wp-login.aspx/','usuario/wp-login.php/','usuario/wp-login.asp/','usuario/wp-login.aspx/','admin/webadmin.asp/','admin/webadmin.aspx/','admin/webadmin.php/'
,'webadmin/user.php/','webadmin/user.asp/','webadmin/user.aspx/','bb-admin/user.php','bb-admin/user.asp','bb-admin/user.aspx','controlpanel/user.php','controlpanel/user.asp','controlpanel/user.aspx'
,'admin-login/user.php','admin-login/user.asp','admin-login/user.aspx','administrator/user.php','administrator/user.asp','administrator/user.aspx','admin/user.php','adm/user.php','pages/moderator.php'
,'webadmin/moderator.php','users/moderator.php','usuario/user.php/','usuario/user.asp/','usuario/user.aspx/','mysql/','myadmin/','sqlmanager/','mysqlmanager/','p/m/a/','phpmanager/','php-myadmin/'
,'phpmy-admin/','sqlweb/','websql/','webdb/','mysqladmin/','mysql-admin/','phpmyadmin2/','phpMyAdmin-2/','php-my-admin/','phpMyAdmin-2.2.3/','phpMyAdmin-2.2.6/','phpMyAdmin-2.5.1/','phpMyAdmin-2.5.4/'
,'phpMyAdmin-2.5.5-rc1/','phpMyAdmin-2.5.5-rc2/','phpMyAdmin-2.5.5/','phpMyAdmin-2.5.5-pl1/','phpMyAdmin-2.5.6-rc1/','phpMyAdmin-2.5.6-rc2/','phpMyAdmin-2.5.6/','phpMyAdmin-2.5.7/','phpMyAdmin-2.5.7-pl1/','phpMyAdmin-2.6.0-alpha/'
,'phpMyAdmin-2.6.0-alpha2/','phpMyAdmin-2.6.0-beta1/','phpMyAdmin-2.6.0-beta2/','phpMyAdmin-2.6.0-rc1/','phpMyAdmin-2.6.0-rc2/','phpMyAdmin-2.6.0-rc3/','phpMyAdmin-2.6.0/','phpMyAdmin-2.6.0-pl1/'
,'phpMyAdmin-2.6.0-pl2/','phpMyAdmin-2.6.0-pl3/','phpMyAdmin-2.6.1-rc1/','phpMyAdmin-2.6.1-rc2/','phpMyAdmin-2.6.1/','phpMyAdmin-2.6.1-pl1/','phpMyAdmin-2.6.1-pl2/','phpMyAdmin-2.6.1-pl3/','phpMyAdmin-2.6.2-rc1/'
,'phpMyAdmin-2.6.2-beta1/','phpMyAdmin-2.6.2/','phpMyAdmin-2.6.2-pl1/','phpMyAdmin-2.6.3/','phpMyAdmin-2.6.3-rc1/','phpMyAdmin-2.6.3-pl1/','phpMyAdmin-2.6.4-rc1/','phpMyAdmin-2.6.4-pl1/','phpMyAdmin-2.6.4-pl2/'
,'phpMyAdmin-2.6.4-pl3/','phpMyAdmin-2.6.4-pl4/','phpMyAdmin-2.6.4/','phpMyAdmin-2.7.0-beta1/','phpMyAdmin-2.7.0-rc1/','phpMyAdmin-2.7.0-pl1/','phpMyAdmin-2.7.0-pl2/','phpMyAdmin-2.7.0/','phpMyAdmin-2.8.0-beta1/'
,'phpMyAdmin-2.8.0-rc2/','phpMyAdmin-2.8.0/','phpMyAdmin-2.8.0.1/','phpMyAdmin-2.8.0.2/','phpMyAdmin-2.8.0.3/','phpMyAdmin-2.8.0.4/','phpMyAdmin-2.8.1-rc1/','phpMyAdmin-2.8.1/','phpMyAdmin-2.8.2/','pma2005/','administratie/'
,'admins.php','useradmin/','sysadmins/','system-administration/','administrators/pgadmin/','directadmin/','sql-admin/','newsadmin/','adminpro/','staradmin/','ServerAdministrator/','SysAdmin/','administer/'
,'LiveUser_Admin/','sys-admin/','autologin/','support_login/','memlogin/','login-redirect/','sub-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/'
,'acct_login/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','bbadmin/','administratoraccounts/','AdminTools/','server/','database_administration/','power_user/','system_administration/','adminitem/','sysadm/'
,'control/','accounts/','management/','phpSQLiteAdmin/','showlogin/','0admin/login.asp','0manager/admin.asp','admin/sendfile.asp,admin/sndfile.asp','admin/upfile.asp','admin/upload.asp','admin/uploadfaceok.asp'
,'admin/uploads.asp','admin/uppic.asp','adminadmin/','adminindex/','count_admin','default_admin','index/admin','acesso/','adimin/','adiministrador/','adm/admin/','admin4_account/','admin4_colon/'
,'admin/adm/','administracao/','banneradmin/','blogindex/','cadmins/','ccp14admin/','cmsadmin/','config/','controle/','cpanel_file/','donos/','edit/','entrar','entrar.html','entrar.php','ezsqliteadmin/'
,'formslogin/','funcoes/','globes_admin/','hpwebjetadmin/','Indy_admin/','irc-macadmin/','key/','logar/','login/','loginflat/','login-us/','loginuser/','loginusuarios/','logo_sysadmin/','logout/'
,'Lotus_Domino_Admin/','macadmin/','manuallogin/','membros/','meta_login/','navSiteAdmin/','net/','not/','openvpnadmin/','painel/','paineldecontrole/','pc/,pdc/','php/','phpldapadmin/','platz_login/'
,'radmind/','radmind-1/','rcLogin/','saff/','senha/','senhas/','server_admin_small/','sff/','simpleLogin/','sistema/','sshadmin/','ss_vms_admin_sm/','Super-Admin/','SysAdmin2/','userlogin/','utility_login/'
,'vadmind/','vmailadmin/','wizmysqladmin/','ccms/','ccms/login.php','ccms/index.php'
]
done = "###################################DONE####################################"
def logo():
    print(Fore.RED+("||||||||||||     |||||||                 |||||||     |||||||     |||||||"))
    print(Fore.RED+("||||||||||||      |||||||               |||||||      |||||||     |||||||"))
    print(Fore.RED+("|||                |||||||             |||||||       |||||||     |||||||"))
    print(Fore.RED+("|||                 |||||||           |||||||        |||||||     |||||||"))
    print(Fore.RED+("||||||||||||         |||||||         |||||||         |||||||     |||||||"))
    print(Fore.RED+("||||||||||||          |||||||       |||||||          |||||||     |||||||"))
    print(Fore.RED+("|||                    |||||||     |||||||           |||||||     |||||||"))
    print(Fore.RED+("|||                     |||||||   |||||||            |||||||     |||||||||||||||||||"))
    print(Fore.RED+("||||||||||||             ||||||| |||||||             |||||||     |||||||||||||||||||"))
    print(Fore.RED+("||||||||||||              |||||||||||||              |||||||     |||||||||||||||||||"))
    print(Fore.RED+"MADE BY MOHAMMADMEHDI.VPN")

while True:
    logo()
    print(Fore.MAGENTA+("ADMIN PAGE FOUNDER CHOSEN!"))
    print(Fore.CYAN+("EXAMPLE: www.example.com ")) 
    url = input (Fore.RED+'ENTER TARGET URL: ')
    if str("https") in str(url):
        pass
    elif str("http") in str(url):
        pass
    else:
        url = ("http://" + url)

    if str(url[-1]) == "/":
        pass
    else:
        url = url + "/"
    try:
        print(Fore.WHITE+"\t CHECLIN URL "+url)
        req = requests.get(url)
        if  req.status_code == 200:
            print(Fore.GREEN+'SERVER IS ONLINE...')
    except:
        print(Fore.RED+'SERVER NOT FOUND...')
    clear()
    logo()
    time.sleep(1)
    print(Fore.WHITE+'\t URL CHOSEN: ' +url)
    print (Fore.GREEN+"1) PHP")
    print (Fore.GREEN+"2) ASP")
    print (Fore.GREEN+"3) CFM")
    print (Fore.GREEN+"4) JS")
    print (Fore.GREEN+"5) CGI")
    print (Fore.GREEN+"6) BRF")
    print (Fore.GREEN+"7) STRONG")
    print (Fore.GREEN+"8) ALL")
    print(Fore.BLUE+("ENTER 'exit' TO BACK MENU"))
    ADMIN_ENTER = input(Fore.RED+("ENTER SITE SOURCE: "))

    if ADMIN_ENTER == "exit":
        clear()
        break
    elif ADMIN_ENTER == '1':
        clear()
        logo()
        print(Fore.MAGENTA+("PHP SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in php:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '2':
        clear()
        logo()
        print(Fore.MAGENTA+("ASP SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in asp:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')


    elif ADMIN_ENTER == '3':
        clear()
        logo()
        print(Fore.MAGENTA+("CFM SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in cfm:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '4':
        clear()
        logo()
        print(Fore.MAGENTA+("JS SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in js:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '5':
        clear()
        logo()
        print(Fore.MAGENTA+("CGI SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in cgi:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '6':
        clear()
        logo()
        print(Fore.MAGENTA+("BRF SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in brf:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '7':
        clear()
        logo()
        print(Fore.MAGENTA+("STRONG SOURCE CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in strong:
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')

    elif ADMIN_ENTER == '8':
        clear()
        logo()
        print(Fore.MAGENTA+("ALL SOURCE  CHOSEN!"))
        time.sleep(1)
        print(Fore.WHITE+"\t SCANNING "+url + "...\n\n")
        var2 = 0
        var1 = 0
        var3 = 0
        for admin in strong + php + js + asp + cfm +cgi + brf :
            admin = admin.replace("\n","")
            
            host = url + admin
            print (Fore.YELLOW+"\t [#] Checking " + host + "...")
            req = requests.get(host)
            var2 = var2 + 1
            if req.status_code == 200:
                var1 = var1 + 1
                FOUND = print(Fore.GREEN+'ADMIN PAGE FOUND: '+host)
            elif req.status_code == 404:
                var2 = var2
                continue
            elif req.status_code == 302:
                var3 = var3 + 1
                POSSIBLE = print(Fore.LIGHTGREEN_EX+'POSSIBLE ADMIN PAGE: '+host)

        var1 = str(var1)
        var2 = str(var2)
        var3 = str(var3)
        print(Fore.LIGHTGREEN_EX+"ADMIN PAGE FOUND: "+var1+'!\n')
        print(Fore.LIGHTGREEN_EX+"POSSIBLE ADMIN PAGE: "+var3+'!\n')
        print(Fore.LIGHTGREEN_EX+"TOTAL PAGE SCANNED: "+var2+'!\n')