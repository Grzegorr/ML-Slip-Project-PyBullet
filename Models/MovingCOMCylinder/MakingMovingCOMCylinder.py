import math
def addCylinderLink(r,h,mass,link_name,lat_friction,a_transparency,material_name):
    text_file.write('<link name= "' + str(link_name) + '" >\n')
    #contact informaion
    text_file.write('\n\t< contact >\n')
    text_file.write('\t\t< lateral_friction value = "' + str(lat_friction) + '" />\n')
    text_file.write('\t\t< spinning_friction value = "0" />\n')
    text_file.write('\t\t< rolling_friction value = "0" />\n')
    text_file.write('\t< /contact >\n')

    text_file.write('\n\t< visual >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< geometry >\n')
    text_file.write('\t\t\t<cylinder radius="' + str(r) + '" length="' + str(h) + '" />\n')
    text_file.write('\t\t< /geometry >\n')
    text_file.write('\t\t< material name = "' + str(material_name) + '" >\n')
    text_file.write('\t\t\t< color rgba = "0.0 0.0 0.1 ' + str(a_transparency) + '"/>\n')
    text_file.write('\t\t< /material >\n')
    text_file.write('\t< /visual >\n\n')

    text_file.write('\n\t< collision >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< geometry >\n')
    text_file.write('\t\t\t<cylinder radius="' + str(r) + '" length="' + str(h) + '" />\n')
    text_file.write('\t\t< /geometry >\n')
    text_file.write('\t< /collision >\n\n')

    text_file.write('\n\t< inertial >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< mass value = "' + str(mass) + '" />\n')
    text_file.write('<inertia ixx="0.0017166666666666667" ixy="0" ixz="0" iyy="0.0017166666666666667" iyz="0" izz="0.0001"/>\n')
    text_file.write('\t< /inertial >\n\n')

    text_file.write('< /link >\n')

def addJoint(parent_link, child_link, joint_name, joint_type,x,y,z,r,p,yaw,low_limit,high_limit):
    text_file.write('\n< joint name = "' + str(joint_name) + '" type = "' + str(joint_type) + '" >\n')
    text_file.write('\t< origin rpy = "' + str(r) + ' ' + str(p) + ' ' + str(yaw) + '" xyz = "' + str(x) + ' ' + str(y) + ' ' + str(z) + '" />\n')
    text_file.write('\t< parent link = "' + str(parent_link) + '" />\n')
    text_file.write('\t< child link = "' + str(child_link) + '" />\n')
    if joint_type == "prismatic":
        text_file.write('\t< limit lower = "' + str(low_limit) + '" upper = "' + str(high_limit) + '" />\n')
        text_file.write('\t< axis xyz = "0 0 1" />\n')
    else:
        text_file.write('\t< axis xyz = "0 0 0" />\n')
    text_file.write('< /joint >\n')

def addBoxLink(link_name, lat_friction, size_x,size_y,size_z,mass,a_transparency):
    text_file.write('<link name= "' + str(link_name) + '" >\n')
    #contact informaion
    text_file.write('\n\t< contact >\n')
    text_file.write('\t\t< lateral_friction value = "' + str(lat_friction) + '" />\n')
    text_file.write('\t\t< spinning_friction value = "0" />\n')
    text_file.write('\t\t< rolling_friction value = "0" />\n')
    text_file.write('\t< /contact >\n')

    text_file.write('\n\t< visual >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< geometry >\n')
    text_file.write('\t\t\t<box size = "' + str(size_x) + ' ' + str(size_y) + ' ' + str(size_z) + '" />\n')
    text_file.write('\t\t< /geometry >\n')
    text_file.write('\t\t< material name = "" >\n')
    text_file.write('\t\t\t< color rgba = "0.0 0.0 0.1 ' + str(a_transparency) + '"/>\n')
    text_file.write('\t\t< /material >\n')
    text_file.write('\t< /visual >\n\n')

    text_file.write('\n\t< collision >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< geometry >\n')
    text_file.write('\t\t\t<box size = "' + str(size_x) + ' ' + str(size_y) + ' ' + str(size_z) + '" />\n')
    text_file.write('\t\t< /geometry >\n')
    text_file.write('\t< /collision >\n\n')

    text_file.write('\n\t< inertial >\n')
    text_file.write('\t\t<origin rpy="0 0 0" xyz = "0 0 0" />\n')
    text_file.write('\t\t< mass value = "' + str(mass) + '" />\n')
    text_file.write('<inertia ixx="0.0017166666666666667" ixy="0" ixz="0" iyy="0.0017166666666666667" iyz="0" izz="0.0001"/>\n')
    text_file.write('\t< /inertial >\n\n')

    text_file.write('< /link >\n')

def addPieceOfWall(size_x,size_y,size_z,mass,lat_friction, a_transparency, angle,r,piece_no,z):
    link_name = "piece" + str(piece_no)
    joint_name = link_name
    addBoxLink(link_name, lat_friction, size_x,size_y,size_z,mass,a_transparency)
    angle = angle * 3.14 / 180
    x = r*math.cos(angle)
    y = r*math.sin(angle)
    yaw = angle
    addJoint("cylinder_top",link_name,joint_name, "fixed",x,y,z,0,0,yaw,0,0)

def addAllSpikes(no_spikes,r):
    for i in range(no_spikes):
        angle = 360.0 * i / no_spikes
        addPieceOfWall(0.05,0.02,0.5,1,0.4, 0.2, angle,r,i,0.25)



text_file = open("COMcylinder.urdf", "w")

text_file.write('<?xml version="1.0" ?>\n')
text_file.write('<robot name="COMcylinder">\n\n')

addCylinderLink(0.2 ,0.05 ,1 ,"cylinder_top" ,0.4 ,0.1,"Siedes_material")
addCylinderLink(0.2 ,0.05 ,1 ,"cylinder_bottom" ,0.4 ,0.1,"Siedes_material")
addJoint("cylinder_top","cylinder_bottom","top_to_bottom", "fixed",0,0,0.5,0,0,0,0,0)
addAllSpikes(90,0.2)
addCylinderLink(0.15 ,0.15 ,5 ,"cylinder_slider" ,0.1 ,1,"slider_material")
addJoint("cylinder_top","cylinder_slider","top_to_slider", "prismatic",0,0,1,0,0,0,0,1)


text_file.write('\n</robot>\n')




text_file.close()

print("Done!")