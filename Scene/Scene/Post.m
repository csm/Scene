//
//  Post.m
//  Scene
//
//  Created by Casey Marshall on 5/28/11.
//  Copyright 2011 Modal Domains. All rights reserved.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.

#import "Post.h"


@implementation Post

@synthesize key;
@synthesize date;
@synthesize message;
@synthesize location;
@synthesize who;
@synthesize avatarId;
@synthesize avatar;

- (id) initWithDictionary: (NSDictionary *) dict
{
    if ((self = [super init]) != nil)
    {
        self.key = (NSString *) [dict objectForKey: kPostKeyDictKey];
        NSDateFormatter *fmt = [[NSDateFormatter alloc] init];
        [fmt setDateFormat: @"yyyy-MM-dd HH:mm:ss"];
        [fmt setTimeZone: [NSTimeZone timeZoneWithName: @"UTC"]];
        self.date = [fmt dateFromString: (NSString *) [dict objectForKey: kPostDateDictKey]];
        [fmt release];
        self.message = (NSString *) [dict objectForKey: kPostMessageDictKey];
        NSArray *loc = (NSArray *) [dict objectForKey: kPostLocationDictKey];
        self.location = CLLocationCoordinate2DMake([[loc objectAtIndex: 0] floatValue],
                                                   [[loc objectAtIndex: 1] floatValue]);
        self.who = (NSString *) [dict objectForKey: kPostNameDictKey];
        self.avatarId = (NSString *) [dict objectForKey: kPostAvatarDictKey];
    }
    return self;
}

- (void) dealloc
{
    [key release];
    [date release];
    [message release];
    [who release];
    [avatarId release];
    [avatar release];
    [super dealloc];
}

@end
