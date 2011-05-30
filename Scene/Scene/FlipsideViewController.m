//
//  FlipsideViewController.m
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

#import "FlipsideViewController.h"
#import <CoreLocation/CoreLocation.h>

@implementation FlipsideViewController

@synthesize delegate=_delegate;

- (void)dealloc
{
    [super dealloc];
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc. that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    [super viewDidLoad];
    //self.view.backgroundColor = [UIColor viewFlipsideBackgroundColor];  
    [locLabel setFont: [UIFont fontWithName: @"DroidSans"
                                       size: 24]];
    [locStatusLabel setFont: [UIFont fontWithName: @"DroidSans-Bold"
                                             size: 24]];
    [locServLabel setFont: [UIFont fontWithName: @"DroidSans"
                                           size: 17]];
    [accountLabel setFont: [UIFont fontWithName: @"DroidSans"
                                           size: 24]];
    [accountInsLabel setFont: [UIFont fontWithName: @"DroidSans"
                                              size: 17]];
    [nameField setFont: [UIFont fontWithName: @"DroidSans"
                                        size: 18]];
    [button.titleLabel setFont: [UIFont fontWithName: @"DroidSans-Bold"
                                                size: 15]];
    [versionLabel setFont: [UIFont fontWithName: @"DroidSans"
                                           size: 15]];
    [copyrightLabel setFont: [UIFont fontWithName: @"DroidSans"
                                             size: 15]];
}

- (void) viewWillAppear:(BOOL)animated
{
    NSLog(@"viewWillAppear:%d", animated);
    [super viewWillAppear: animated];
    if (![CLLocationManager locationServicesEnabled]
        || [CLLocationManager authorizationStatus] != kCLAuthorizationStatusAuthorized)
    {
        [locStatusLabel setText: @"OFF"];
        [locStatusLabel setTextColor: [UIColor colorWithRed:0.502 green:0.000 blue:0.000 alpha:1.000]];
    }
    else
    {
        [locStatusLabel setText: @"ON"];
        [locStatusLabel setTextColor: [UIColor colorWithRed:0.000 green:0.502 blue:0.000 alpha:1.000]];
    }
}

- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    // Return YES for supported orientations
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}

#pragma mark - Actions

- (IBAction)done:(id)sender
{
    [self.delegate flipsideViewControllerDidFinish:self];
}

@end
