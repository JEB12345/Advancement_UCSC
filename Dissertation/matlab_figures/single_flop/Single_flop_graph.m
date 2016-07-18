% This should make the single flop graph showing CoM and Bottom node
% positions

load('single_cable_flop.mat');
n = 89; % Change this to set middle point

figure()
plot(node_data(2,1),node_data(2,2),'o')
hold on
plot(node_data(4,1),node_data(4,2),'o')
plot(node_data(11,1),node_data(11,2),'o')
plot(com_x(1),com_y(1),'o')

plot(node_data(4,1:3:(n*3)),node_data(4,2:3:(n*3)),'.')
plot(node_data(2,1:3:(n*3)),node_data(2,2:3:(n*3)),'.')
plot(node_data(11,1:3:(n*3)),node_data(11,2:3:(n*3)),'.')
plot(com_x(1:n),com_y(1:n),'.')

line([node_data(2,(n*3)-2),node_data(11,(n*3)-2)],[node_data(2,(n*3)-1),node_data(11,(n*3)-1)],'color',[1 0 0])
line([node_data(4,(n*3)-2),node_data(11,(n*3)-2)],[node_data(4,(n*3)-1),node_data(11,(n*3)-1)],'color',[1 0 0])
line([node_data(4,(n*3)-2),node_data(2,(n*3)-2)],[node_data(4,(n*3)-1),node_data(2,(n*3)-1)],'color',[1 0 0])
line([node_data(2,(3)-2),node_data(11,(3)-2)],[node_data(2,(3)-1),node_data(11,(3)-1)])
line([node_data(4,(3)-2),node_data(11,(3)-2)],[node_data(4,(3)-1),node_data(11,(3)-1)])
line([node_data(4,(3)-2),node_data(2,(3)-2)],[node_data(4,(3)-1),node_data(2,(3)-1)])
axis('equal')