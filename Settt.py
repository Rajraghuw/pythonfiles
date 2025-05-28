#unorderd collection of uniq elements
#represent through {} with comma seprated objects.
#indexing not supported.
#slicing not supported.
#mutable in nature.
#jitni bar run krenge utni bar iska order change hoga isi liye ye unorderd collection hai 

#Ex---->

# st={2,4,6,5,8,'python','java'}
# print(st)


#python methoud--->


# st={2,4,6,5,8,'python','java'}
# print(len(st))
# print(id(st))
# print(type(st))

#in-build methouds--->
# add()---
# update()--->(multiple value add karne ke liye or ye sirf collection add karta h )
# pop()--->>(rendome number remove)
# remove()
# discart()---------->>(discart remove karta h agr wo element nhi h tab v ye error mhi deta age element hai to remove kar deta hai)
# clear()
# copy()
# union()
# intersection()
# diffence()
# symmetric difference()
# diffence update()
# symmetric_diffence-update()

#add methoud---->

# s={2,4,6,5,8,'python','java'}
# s.add('php')
# print(s)

#update methoud---->

# s={2,4,6,5,8,'python','java'}
# s.update('python')
# print(s)

# s={2,4,6,5,8,'python','java'}
# s.update((1,3,7,9))
# print(s)


# s={2,4,6,5,8,'python','java'}
# s.update((1,3,'raja'),'python')
# print(s)

#pop-------->
# s={2,4,6,5,8,'python','java'}
# s.pop()
# print(s)

#remove---->

# s={2,4,6,5,8,'python','java'}
# s.remove('python')
# print(s)

#discart----->

# s={2,4,6,5,8,'python','java'}
# s.discard('python')
# print(s)


#clear--->
# s={2,4,6,5,8,'python','java'}
# s.clear()
# print(s)

#copy---->

# s={2,4,6,5,8,'python','java'}
# s1=s.copy()
# print(s,s1)
# print(id(s),id(s1))





#union----->
# s1={1,2,3,4,5}
# s2={2,6,5,3,4}
# print(s1.union(s2))


#interction--->

# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# print(s1.intersection(s2))


# #diffence--->

# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# print(s1.difference(s2))


# #symettric diffence --->

# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# print(s1.symmetric_difference(s2))


#interction update--->

# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# s1.intersection_update(s2)
# print(s1)
# print(s2)


#diffence update---->

# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# s1.difference_update(s2)
# print(s1)
# print(s2)


#simmetric update --->>
# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# s1.symmetric_difference_update(s2)
# print(s1)
# print(s2)


#is disgeint---->
# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# print(s1.disjoint(s2))


#is superset--->
# s1={1,2,3,4,5}
# s2={6,5,6,5,4,7}
# print(s1.issubset(s2))



