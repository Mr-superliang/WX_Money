#导入mx模块
import wx
import wx.grid
from mydb import Sql_operation
#创建资金管理系统登录界面类
class UserLogin(wx.Frame):
	'''
	登录界面
	'''
	#初始化登录界面
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(UserLogin,self).__init__(*args, **kw)
		#设置窗口屏幕居中
		self.Center()
		#创建窗口
		self.pnl = wx.Panel(self)
		#调用登录界面函数
		self.LoginInterface()

	def LoginInterface(self):
		#创建垂直方向box布局管理器
		vbox = wx.BoxSizer(wx.VERTICAL)
		#################################################################################
		#创建logo静态文本，设置字体属性
		logo = wx.StaticText(self.pnl,label="个人资金管理系统")
		font = logo.GetFont()
		font.PointSize += 30
		font = font.Bold()
		logo.SetFont(font)
		#添加logo静态文本到vbox布局管理器
		vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=180)
		#################################################################################
		#创建静态框
		sb_username = wx.StaticBox(self.pnl,label="用户名")
		sb_password = wx.StaticBox(self.pnl,label="密  码")		
		#创建水平方向box布局管理器
		hsbox_username = wx.StaticBoxSizer(sb_username,wx.HORIZONTAL)
		hsbox_password = wx.StaticBoxSizer(sb_password,wx.HORIZONTAL)
		#创建用户名、密码输入框
		self.user_name = wx.TextCtrl(self.pnl,size=(210,25))
		self.user_password = wx.TextCtrl(self.pnl,size=(210,25))
		#添加用户名和密码输入框到hsbox布局管理器
		hsbox_username.Add(self.user_name,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_password.Add(self.user_password,0,wx.EXPAND | wx.BOTTOM,5)
		#将水平box添加到垂直box
		vbox.Add(hsbox_username,proportion=0,flag=wx.CENTER)
		vbox.Add(hsbox_password,proportion=0,flag=wx.CENTER)
		#################################################################################
		#创建水平方向box布局管理器
		hbox = wx.BoxSizer()
		#创建登录按钮、绑定事件处理
		login_button = wx.Button(self.pnl,label="登录",size=(80,25))
		login_button.Bind(wx.EVT_BUTTON,self.LoginButton)
		#添加登录按钮到hbox布局管理器
		hbox.Add(login_button,0,flag=wx.EXPAND | wx.TOP,border=5)
		#将水平box添加到垂直box
		vbox.Add(hbox,proportion=0,flag=wx.CENTER)
		#################################################################################
		#设置面板的布局管理器vbox		
		self.pnl.SetSizer(vbox)		

	def LoginButton(self,event):
		#连接login_users数据库
		op = Sql_operation("login_users")
		#获取users表中的用户名和密码信息，返回为二维元组
		np = op.FindAll("users")
		#匹配标记
		login_sign = 0
		#匹配用户名和密码
		for i in np:
			if (i[1] == self.user_name.GetValue()) and (i[2] == self.user_password.GetValue()):
				login_sign = 1
				break
		if login_sign == 0:
			print("用户名或密码错误！")
		elif login_sign == 1:
			# print("登录成功！")			
			operation = UserOperation(None,title="资金管理系统",size=(1024,668))
			operation.Show()
			self.Close(True)


class UserOperation(wx.Frame):
	'''
	操作界面
	'''
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(UserOperation,self).__init__(*args, **kw)
		#设置窗口屏幕居中
		self.Center()
		#创建窗口
		self.pnl = wx.Panel(self)
		#调用操作界面函数
		self.OperationInterface()

	def OperationInterface(self):
		#创建垂直方向box布局管理器
		self.vbox = wx.BoxSizer(wx.VERTICAL)		
		#################################################################################
		#创建logo静态文本，设置字体属性
		logo = wx.StaticText(self.pnl,label="资金管理系统")
		font = logo.GetFont()
		font.PointSize += 30
		font = font.Bold()
		logo.SetFont(font)
		#添加logo静态文本到vbox布局管理器
		self.vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=5)
		#################################################################################
		#创建静态框
		sb_button = wx.StaticBox(self.pnl,label="操作选择")
		#创建垂直方向box布局管理器
		vsbox_button = wx.StaticBoxSizer(sb_button,wx.VERTICAL)
		#创建操作按钮、绑定事件处理
		check_button = wx.Button(self.pnl,id=10,label="查看资金信息",size=(150,50))
		add_button = wx.Button(self.pnl,id=11,label="添加资金信息",size=(150,50))
		delete_button = wx.Button(self.pnl,id=12,label="删除资金信息",size=(150,50))
		quit_button = wx.Button(self.pnl,id=13,label="退出系统",size=(150,50))
		self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=13)
		#添加操作按钮到vsbox布局管理器
		vsbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,40)
		vsbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,40)
		vsbox_button.Add(delete_button,0,wx.EXPAND | wx.BOTTOM,40)
		vsbox_button.Add(quit_button,0,wx.EXPAND | wx.BOTTOM,200)		
		#创建静态框
		sb_show_operation = wx.StaticBox(self.pnl,label="显示/操作窗口",size=(800,500))
		#创建垂直方向box布局管理器
		self.vsbox_show_operation = wx.StaticBoxSizer(sb_show_operation,wx.VERTICAL)
		#创建水平方向box布局管理器
		hbox = wx.BoxSizer()
		hbox.Add(vsbox_button,0,wx.EXPAND | wx.BOTTOM,5)
		hbox.Add(self.vsbox_show_operation,0,wx.EXPAND | wx.BOTTOM,5)
		#将hbox添加到垂直box		
		self.vbox.Add(hbox,proportion=0,flag=wx.CENTER)		
		#################################################################################
		self.pnl.SetSizer(self.vbox)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			# print("查询操作！")
			inquire_button = InquireOp(None,title="资金信息管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			# print("添加操作！")
			add_button = AddOp(None,title="资金信息管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			# print("删除操作！")
			del_button = DelOp(None,title="资金信息管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)			
		elif source_id == 13:
			self.Close(True)

#继承UserOperation类，实现初始化操作界面
class InquireOp(UserOperation):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(InquireOp,self).__init__(*args, **kw)
		#创建资金信息网格		
		self.stu_grid = self.CreateGrid()			
		self.stu_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.OnLabelleftClick)
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(self.stu_grid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,30)		

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			pass						
		elif source_id == 11:
			# print("添加操作！")
			add_button = AddOp(None,title="资金管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			# print("删除操作！")
			del_button = DelOp(None,title="资金管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)			
		elif source_id == 13:
			self.Close(True)

	def CreateGrid(self):
		#连接login_users数据库
		op = Sql_operation("login_users")
		#获取money_info表中的资金信息，返回为二维元组
		np = op.FindAll("money_info")
		column_names = ("总金额","机构名称","已用金额","剩余金额","还款日期","应还金额")
		stu_grid = wx.grid.Grid(self.pnl)
		stu_grid.CreateGrid(len(np),len(np[0])-1)
		for row in range(len(np)):
			stu_grid.SetRowLabelValue(row,str(np[row][0]))#确保网格序列号与数据库id保持一致
			for col in range(1,len(np[row])):
				stu_grid.SetColLabelValue(col-1,column_names[col-1])				
				stu_grid.SetCellValue(row,col-1,str(np[row][col]))				
		stu_grid.AutoSize()
		return stu_grid

	def OnLabelleftClick(self,event):
		#连接login_users数据库
		op = Sql_operation("login_users")
		#获取users表中的用户名和密码信息，返回为二维元组
		np = op.FindAll("money_info")
		print("RowIdx: {0}".format(event.GetRow()))
		print("ColIdx: {0}".format(event.GetRow()))
		print(np[event.GetRow()])
		event.Skip()

#继承UserOperation类，实现初始化操作界面
class AddOp(UserOperation):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(AddOp,self).__init__(*args, **kw)
		#创建添加资金信息输入框、添加按钮
		self.total_amount = wx.TextCtrl(self.pnl,size = (210,25))
		self.institution_name = wx.TextCtrl(self.pnl,size = (210,25))
		self.used_amount = wx.TextCtrl(self.pnl,size = (210,25))
		# self.balance = wx.TextCtrl(self.pnl,size = (210,25))
		self.repayment_date = wx.TextCtrl(self.pnl,size = (210,25))
		# self.amount_due = wx.TextCtrl(self.pnl,size = (210,25))
		self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)
		#################################################################################
		#创建静态框
		sb_total_amount = wx.StaticBox(self.pnl,label="总金额")
		sb_institution_name = wx.StaticBox(self.pnl,label="机构名称")
		sb_used_amount = wx.StaticBox(self.pnl,label="已用金额")
		# sb_balance = wx.StaticBox(self.pnl,label="剩余金额")
		sb_repayment_date = wx.StaticBox(self.pnl,label="还款日期")
		# sb_amount_due = wx.StaticBox(self.pnl,label="应还金额")		
		#创建水平方向box布局管理器
		hsbox_total_amount = wx.StaticBoxSizer(sb_total_amount,wx.HORIZONTAL)
		hsbox_institution_name = wx.StaticBoxSizer(sb_institution_name,wx.HORIZONTAL)
		hsbox_used_amount = wx.StaticBoxSizer(sb_used_amount,wx.HORIZONTAL)
		# hsbox_balance = wx.StaticBoxSizer(sb_balance,wx.HORIZONTAL)
		hsbox_repayment_date = wx.StaticBoxSizer(sb_repayment_date,wx.HORIZONTAL)
		# hsbox_amount_due = wx.StaticBoxSizer(sb_amount_due,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hsbox_total_amount.Add(self.total_amount,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_institution_name.Add(self.institution_name,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_used_amount.Add(self.used_amount,0,wx.EXPAND | wx.BOTTOM,5)
		# hsbox_balance.Add(self.balance,0,wx.EXPAND | wx.BOTTOM,5)
		hsbox_repayment_date.Add(self.repayment_date,0,wx.EXPAND | wx.BOTTOM,5)
		# hsbox_amount_due.Add(self.amount_due,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(hsbox_total_amount,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_institution_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_used_amount,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		# self.vsbox_show_operation.Add(hsbox_balance,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(hsbox_repayment_date,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		# self.vsbox_show_operation.Add(hsbox_amount_due,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			# print("查询操作！")
			inquire_button = InquireOp(None,title="资金信息管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			pass						
		elif source_id == 12:
			# print("删除操作！")
			del_button = DelOp(None,title="资金信息管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)			
		elif source_id == 13:
			self.Close(True)

	def AddAffirm(self,event):
		#连接login_users数据库
		op = Sql_operation("login_users")
		#向money_info表添加资金信息
		total_amount = self.total_amount.GetValue()
		# print(total_amount)
		institution_name = self.institution_name.GetValue()
		# print(institution_name)
		used_amount = self.used_amount.GetValue()
		# print(used_amount)
		# balance = self.balance.GetValue()
		balance = float(total_amount) - float(used_amount)
		# print(balance)		
		repayment_date = self.repayment_date.GetValue()
		# print(repayment_date)
		# amount_due = self.amount_due.GetValue()
		amount_due = float(total_amount) - float(used_amount)
		# print(amount_due)
		np = op.Insert(total_amount,institution_name,used_amount,balance,repayment_date,amount_due)

#继承InquireOp类，实现初始化操作界面
class DelOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(DelOp,self).__init__(*args, **kw)
		#创建删除学员信息输入框、删除按钮
		self.del_id = wx.TextCtrl(self.pnl,pos = (407,78),size = (210,25))
		self.del_affirm = wx.Button(self.pnl,label="删除",pos=(625,78),size=(80,25))
		#为删除按钮组件绑定事件处理
		self.del_affirm.Bind(wx.EVT_BUTTON,self.DelAffirm)
		#################################################################################
		#创建静态框
		sb_del = wx.StaticBox(self.pnl,label="请选择需要删除的信息id")
		#创建水平方向box布局管理器
		hsbox_del = wx.StaticBoxSizer(sb_del,wx.HORIZONTAL)
		#添加到hsbox_total_amount布局管理器
		hsbox_del.Add(self.del_id,0,wx.EXPAND | wx.BOTTOM,5)
		#添加到vsbox_show_operation布局管理器
		self.vsbox_show_operation.Add(hsbox_del,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vsbox_show_operation.Add(self.del_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		source_id = event.GetId()
		if source_id == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="资金信息管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)			
		elif source_id == 11:
			print("添加操作！")
			add_button = AddOp(None,title="资金信息管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)						
		elif source_id == 12:
			pass		
		elif source_id == 13:
			self.Close(True)

	def DelAffirm(self,event):
		#连接login_users数据库
		op = Sql_operation("login_users")
		#向money_info表添加资金信息
		del_id = self.del_id.GetValue()
		print(del_id)
		np = op.Del(int(del_id))
		
		del_button = DelOp(None,title="资金信息管理系统",size=(1024,668))
		del_button.Show()
		self.Close(True)

if __name__ == '__main__':
	app = wx.App()
	login = UserLogin(None,title="资金信息管理系统",size=(1024,668))
	login.Show()
	app.MainLoop()
